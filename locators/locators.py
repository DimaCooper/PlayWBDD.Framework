# Example locators SOME_BUTTON = (friendly_name, element_name)
# classes are needed to visually separate locators
class BaseLocators:
    
    SUBMIT_BUTTON = ("Submit button", "#submit-btn")
    MENU_ICON = ("Menu icon", ".menu-icon")
    SEARCH_INPUT = ("Search-input", "xpath=//input[contains(@placeholder, 'Поиск')]")
    PREFERENCES_BUTTON = ("Preferences-button", "[href='/ru/flows/develop/']")

class AuthLocators:
    
    LOGIN_BUTTON = ("Login button", "#login-btn")

class ProfileLocators:
    
    PROFILE_LINK = ("Profile link", "text=Profile")
 