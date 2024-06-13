def createBatch(records):
    #Max Record Size = 1MB
    max_record_size = 1024 * 1024
    #Max Batch Size = 5MB
    max_batch_size = 5 * 1024 * 1024
    #Max Records per batch = 500
    max_records_per_batch = 500
    
    current_batch = []
    current_batch_size = 0
    batches = []
    
    for record in records:
        # Assuming that record can be str but not have to
        record_size = len(str(record.encode('utf-8')))
        
        # Check if the record exceeds the maximum size, discard if it does or it is empty
        if record_size > max_record_size or record_size==0:
            continue
        
        # Check if adding the record exceeds the maximum batch size or maximum records per batch
        if (current_batch_size + record_size > max_batch_size) or (len(current_batch) >= max_records_per_batch):
            print(current_batch_size)
            # Start a new batch
            batches.append(current_batch)
            current_batch = []
            current_batch_size = 0
        
        # Add the record to the current batch
        current_batch.append(record)
        current_batch_size += record_size
    
    # Add the last batch (if any)
    if current_batch:
        batches.append(current_batch)
    
    return batches

