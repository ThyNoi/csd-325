# Eric Sengvanhpheng
# July 9, 2026
# Advanced Python Module 7.2

# function that formats parameters
def get_formatted_name(city_name, country_name, population='', language=''):
    
    # capitolize only the city, country, and language
    city_name = city_name.title()
    country_name = country_name.title()
    language = language.title()

    # build the formatted string based on provided arguments, if/else checks
    if population and language:
        full_name = f"{city_name}, {country_name} - population {population}, {language}"
    
    elif population:
        full_name = f"{city_name}, {country_name} - population {population}"
        
    else:
        full_name = f"{city_name}, {country_name}"            
    
    # passes the function's result back to the caller
    return full_name

# run the examples only when this file is executed directly   
if __name__ == '__main__':

    # orignial values 
    # 'santiago', 'chile', '5000000', 'spanish'
    # 'tokyo', 'japan', '37000000', 'japanese'
    # 'dublin', 'ireland', '2000000', 'english'

    result1 = get_formatted_name('santiago', 'chile')
    print(result1)

    result2 = get_formatted_name('tokyo', 'japan', '37000000')
    print(result2)

    result3 = get_formatted_name('dublin', 'ireland', '2000000', 'english')
    print(result3)


