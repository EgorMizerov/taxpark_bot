class CallbackEnum:
    RETURN_MAIN_MENU: str = 'return_main_menu_pressed'
    RETURN_BACK: str = 'return_back_pressed'

    # Главное меню
    GO_TO_CURRENT_ORDER: str = 'go_to_current_order_pressed'
    GO_TO_USER_STATISTICS: str = 'go_to_statistics_pressed'
    GO_TO_PROFILE_MANAGER: str = 'go_to_profile_manager_pressed'
    GO_TO_PROMOTION_STATISTICS: str = 'go_to_promotion_statistics_pressed'
    GO_TO_INFO_AND_HELP: str = 'go_to_info_and_help_pressed'
    GO_TO_FAQ: str = 'go_to_faq_pressed'
    GO_TO_SUBSCRIPTION_SERVICES: str = 'go_to_subscription_services_pressed'
    START_SHIFT: str = 'start_shift_pressed'

    # Текущий заказ
    CANCEL_FINISHED_ORDER: str = 'cancel_finished_order_pressed'
    CANCEL_NOT_FINISHED_ORDER: str = 'cancel_not_finished_order_pressed'

    # Статистика пользователя
    STATISTICS_PERIOD: str = 'statistics_period_pressed'
    STATISTICS_VARIANTS: str = 'statistics_variants_pressed'

    # Бонусы и акции
    PROMOTIONS_INFO: str = 'promotions_info_pressed'
    COPY_REFERAL: str = 'copy_referal_pressed'
    REFER_FRIEND: str = 'refer_friend_pressed'
    NO_COMMISSION_MONTH: str = 'no_commission_month_pressed'
