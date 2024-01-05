from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('the chatbot is running')
def step_impl(context):
    # Iniciar el servidor Flask en segundo plano
    from subprocess import Popen, PIPE
    context.server = Popen(['python', 'app.py'], stdout=PIPE)

    # Esperar un tiempo para que el servidor se inicie completamente
    import time
    time.sleep(2)


@when('the user sends a message "{message}"')
def step_impl(context, message):
    # Abrir la página del chatbot en el navegador
    context.driver.get('http://localhost:5000')

    # Enviar el mensaje al chatbot
    input_element = context.driver.find_element_by_id('message-input')
    input_element.send_keys(message)
    input_element.send_keys(Keys.ENTER)

@then('the chatbot should respond with "{expected_response}"')
def step_impl(context, expected_response):
    # Esperar a que el chatbot genere la respuesta
    import time
    time.sleep(2)

    # Obtener la respuesta del chatbot
    response_element = context.driver.find_element_by_id('response')
    actual_response = response_element.text

    # Verificar que la respuesta sea la esperada
    assert actual_response == expected_response

@step('teardown')
def step_impl(context):
    # Cerrar el navegador y detener el servidor Flask
    context.driver.quit()
    context.server.terminate()
