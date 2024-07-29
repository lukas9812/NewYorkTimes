class ApiMethods:

    def get_book_properties(apiData, property):
        properties = []
        for item in apiData:
            properties.append(item[property])

        return properties
        
    
