def count_nested_levels(nested_documents, target_document_id, level=1):
    result = -1
    for id,val in nested_documents.items():
        if id == target_document_id:
            result = level
            return result
        elif id != target_document_id and len(val)== 1 and isinstance(val,dict):
            result = count_nested_levels(val,target_document_id,level=level+1)
    
    return result
