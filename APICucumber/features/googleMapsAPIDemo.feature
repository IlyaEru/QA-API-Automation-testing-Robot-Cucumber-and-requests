Feature: Verify if places are added and deleted using Google Maps API

  @googleMaps
  Scenario: Verify adding place API functionality
    Given the place details which needs to be added to the server
    When we execute the Google Maps PostAPI method
    Then place is successfully added
