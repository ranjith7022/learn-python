def count_nested_levels(nested_documents, target_document_id, level=1):
    result = -1
    for id,val in nested_documents.items():
        if id == target_document_id:
            result = level
            return result
        elif isinstance(val,dict):
            result = count_nested_levels(val,target_document_id,level=level+1)
            if result != -1:
                return result
    
    return result