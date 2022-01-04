*** Settings ***
Documentation    Pet Store Api test demo
Library          RequestsLibrary
Resource         apiData.robot
Library          OperatingSystem
Library          Collections

*** Test Cases ***
Add and then Delete new pet to the store
    Add new pet to the pet store
    Delete the added pet

*** Keywords ***
Add new pet to the pet store
    ${add_pet_json_file}          Get file     payloads\\addPetJSON.json
    ${add_body} =   Evaluate   json.loads('''${add_pet_json_file}''')    json
    ${add_response}=    POST    ${base_url}${add_pet_resource}      json=${add_body}
    Should Be Equal As Strings      ${add_response}     <Response [200]>
    log       ${add_response}
    ${book_id}=         get from dictionary     ${add_response.json()}   id
    Set Global Variable     ${book_id}
Delete the added pet
    ${delete_response}=    DELETE    ${base_url}${delete_pet_resource}${book_id}
    Should Be Equal As Strings       ${delete_response.json()}["code"]     200