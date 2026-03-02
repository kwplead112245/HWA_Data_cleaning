import pandas as pd
from fuzzywuzzy import fuzz, process

# Email Matching Function

def match_email(email1, email2):
    """Use simple string matching and domain-level matching for emails"""
    return email1.lower().strip() == email2.lower().strip() or \
           email1.split('@')[-1] == email2.split('@')[-1]


# Address Fuzzy Matching Function

def match_address(address1, address2):
    """Allow fuzzy matching for addresses using fuzzywuzzy"""
    return fuzz.token_set_ratio(address1, address2) > 80


# Improved `find_person` Logic

def find_person(df, email, address):
    """Find a person in a DataFrame based on email and address. Uses fuzzy logic for address."""
    matched = df[(df['email'].apply(match_email, args=(email,)))]
    if matched.empty:
        return None
    # Further match based on address if needed
    matched = matched[matched['address'].apply(match_address, args=(address,))]  
    
    if not matched.empty:
        return matched.iloc[0]
    return None


# Further improvements might be needed based on use cases and data specifics.