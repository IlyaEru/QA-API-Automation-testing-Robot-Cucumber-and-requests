*** Settings ***
Documentation    data for the api tests
Library          JSONLibrary
Library          OperatingSystem
*** Variables ***
${base_url}                 https://petstore.swagger.io/v2
${add_pet_resource}         /pet
${delete_pet_resource}         /pet/
