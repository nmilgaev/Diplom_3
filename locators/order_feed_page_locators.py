from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    # Последний заказ
    LAST_ORDER = (
        By.XPATH,
        "//body/div[@id='root']/div[@class='App_App__aOmNj']/main[@class='App_componentContainer__2JC2W']/div[@class='OrderFeed_orderFeed__2RO_j']/div[@class='OrderFeed_contentBox__3-tWb']/ul[@class='OrderFeed_list__OLh59']/li[1]/a[1]/div[1]"
    )

    # Состав после нажатия на последний заказ
    ORDER_DETAILS_CONTENT = (
        By.XPATH,
        "//p[@class='text text_type_main-medium mb-8']"
    )

    # Счётчик "за всё время" (должен увеличиваться при создании заказа)
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/p[2]"
    )

    # Счётчик "Выполнено за сегодня" (должен увеличиваться при создании заказа)
    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    )

    CLOSE_ORDER_DETAILS_BUTTON = (By.XPATH, "//button[@type='button']//*[name()='svg']")

    ORDER_ID = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/h2[1]")

    ORDER_ID_IN_FEED = (By.XPATH, "//*[contains(text(), '{0}')]")

    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[1]"
    )

