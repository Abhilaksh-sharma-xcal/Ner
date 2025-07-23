import pandas as pd
import spacy
from difflib import SequenceMatcher
from collections import defaultdict

# Load spacy model
nlp = spacy.load("en_core_web_sm")

def extract_pos_filtered_terms(text):
    """Extract meaningful terms using POS filtering"""
    doc = nlp(text)
    terms = []
    
    for token in doc:
        if (token.pos_ in ['NOUN', 'ADJ', 'PROPN'] and 
            not token.is_stop and 
            not token.is_punct and 
            len(token.text) > 1):
            terms.append({
                'text': token.text,
                'lemma': token.lemma_,
                'pos': token.pos_
            })
    
    return terms

def evaluate_against_csv_ground_truth(pos_filtered_terms, ground_truth_df, 
                                    partial_threshold=0.7, semantic_threshold=0.8):

    results = {
        'exact_matches': [],
        'lemma_matches': [],
        'partial_matches': [],
        'semantic_matches': [],
        'no_matches': []
    }
    
    # Prepare ground truth data
    ground_truth_conditions = ground_truth_df['condition'].str.lower().tolist()
    
    # Get synonyms if available in CSV
    synonyms_list = []
    if 'synonyms' in ground_truth_df.columns:
        for synonyms in ground_truth_df['synonyms'].dropna():
            if isinstance(synonyms, str):
                synonyms_list.extend([s.strip().lower() for s in synonyms.split(';')])
    
    # Process each extracted term
    for term_data in pos_filtered_terms:
        term = term_data['text'].lower()
        lemma = term_data['lemma'].lower()
        pos = term_data['pos']
        
        matched = False
        
        # Level 1: Exact matching
        if term in ground_truth_conditions:
            results['exact_matches'].append({
                'extracted_term': term,
                'matched_with': term,
                'match_type': 'exact',
                'pos': pos
            })
            matched = True
            
        # Level 2: Lemmatized matching (stress vs stressed)
        elif not matched:
            for gt_condition in ground_truth_conditions:
                gt_doc = nlp(gt_condition)
                gt_lemmas = [token.lemma_.lower() for token in gt_doc if not token.is_stop]
                
                if lemma in gt_lemmas:
                    results['lemma_matches'].append({
                        'extracted_term': term,
                        'extracted_lemma': lemma,
                        'matched_with': gt_condition,
                        'match_type': 'lemma',
                        'pos': pos
                    })
                    matched = True
                    break
        
        # Level 3: Partial matching (acute bronchitis vs bronchitis)
        if not matched:
            best_partial_match = None
            best_similarity = 0
            
            # Check against main conditions
            for gt_condition in ground_truth_conditions:
                # Substring matching
                if term in gt_condition or gt_condition in term:
                    similarity = max(
                        SequenceMatcher(None, term, gt_condition).ratio(),
                        len(set(term.split()) & set(gt_condition.split())) / 
                        max(len(set(term.split())), len(set(gt_condition.split())))
                    )
                    
                    if similarity >= partial_threshold and similarity > best_similarity:
                        best_similarity = similarity
                        best_partial_match = gt_condition
            
            if best_partial_match:
                results['partial_matches'].append({
                    'extracted_term': term,
                    'matched_with': best_partial_match,
                    'similarity': best_similarity,
                    'match_type': 'partial',
                    'pos': pos
                })
                matched = True
        
        # Level 4: Semantic matching (using synonyms if available)
        if not matched and synonyms_list:
            best_semantic_match = None
            best_similarity = 0
            
            for synonym in synonyms_list:
                similarity = SequenceMatcher(None, term, synonym).ratio()
                
                if similarity >= semantic_threshold and similarity > best_similarity:
                    best_similarity = similarity
                    best_semantic_match = synonym
            
            if best_semantic_match:
                results['semantic_matches'].append({
                    'extracted_term': term,
                    'matched_with': best_semantic_match,
                    'similarity': best_similarity,
                    'match_type': 'semantic',
                    'pos': pos
                })
                matched = True
        
        # Track unmatched terms
        if not matched:
            results['no_matches'].append({
                'extracted_term': term,
                'lemma': lemma,
                'pos': pos
            })
    
    return results


