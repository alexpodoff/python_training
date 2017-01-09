Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <name>, <lastname>, <home> and <email>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | name  | lastname  | home      | email            |
  | name1 | lastname1 | 929383881 | some_email1@m.ru |
  | name2 | lastname2 | 929383882 | some_email2@m.ru |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact