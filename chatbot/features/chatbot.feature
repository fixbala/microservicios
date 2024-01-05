Feature: Chatbot

  Scenario: User interaction
    Given the chatbot is running
    When the user sends a message "Hello"
    Then the chatbot should respond with "¡Hola! ¿En qué puedo ayudarte hoy?"
