idef process_query(vec):
    nearVector = {"vector": vec}
    res = client.query.get("Post", ["content", "_additional {certainty}"]).with_near_vector(nearVector).do()
    print(res)
    print("------------------------------------------------------------------------------------------------")
    print("-----------------------------------Most similar text -------------------------------------------")
    print(res['data']['Get']['Post'][0]['content'])
    print("------------------------------------------------------------------------------------------------")

while True:
    
    query = input("Enter query:")
    if query=='q':
        break

    query_vec = sbert_model.encode(query)
    process_query(query_vec)
