Feature: Careers Search
  As a user
  I want to search for "<University>" on Google
  So that I can see the search results page
  Then I want to click on the first result
  So that I can see the landing page
  Then I want to click on the Careers section
  So that I can see the options they offer.

  Scenario Outline: Searching for Universities Careers on Google
    Given I am on the Google homepage
    When I search for "<University>"
    Then the results page title should start with "<University>"
    And I click on "<University>"
    Then the new page title should start with "<LandingPageTitle>"
    Then inside the page I click on "<CareersSection>"


Examples:
    | University                 | LandingPageTitle                     | CareersSection   |
    | ITESO                      | Home                                 | Carreras         |
    | Tecnológico de Monterrey   | Inicio                               | Oferta educativa |
    | Universidad de Guadalajara | Inicio \| Universidad de Guadalajara | Oferta académica |
