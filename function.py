def send_lead(arguments):
    import requests
    import json

    def get_val(key, def_val=''):
        if key in arguments.keys():
            return arguments[key]
        else:
            return def_val

    result = ''

    url = '##LeadsBitrixWebhook##/crm.lead.add.json'
    if url != '/crm.lead.add.json':
        params = {
            'fields': {
                'TITLE': f"Заявка от клиента: {get_val('sender_socialId')}",
                'WEB': [{'VALUE': get_val('url'), 'VALUE_TYPE': 'WORK'}],
                'COMMENTS':
                    f"""
                    Клиент:
                    Фамилия: {get_val('surname')}
                    Имя: {get_val('name')}
                    Отчество: {get_val('patronymic')}
                    Мобильный телефон: {get_val('mobile_phone')}
                    Дополнительный телефон: {get_val('additional_phone')}
                    Email: {get_val('email')}

                    Паспортные данные:
                    Дата рождения: {get_val('date_of_birth')}
                    Личный номер: {get_val('personal_number')}

                    Сведения о лизинге:
                    Наименование предмета лизинга: {get_val('leasing_subject_name')}
                    Стоимость: {get_val('cost')}
                    Количество: {get_val('quantity')}
                    Аванс: {get_val('advance')}
                    Валюта договора: {get_val('contract_currency')}
                    Срок договора: {get_val('contract_term')}

                    Персональные данные:
                    Место рождения: {get_val('place_of_birth')}
                    Пол: {get_val('gender')}
                    Судимость: {get_val('conviction')}
                    Документ: {get_val('document')}
                    Гражданство: {get_val('citizenship')}
                    Серия: {get_val('series')}
                    Номер: {get_val('number')}
                    Дата Выдачи: {get_val('issue_date')}
                    Срок действия: {get_val('validity_period')}
                    Кем выдан: {get_val('issued_by')}

                    Адрес регистрации:
                    Индекс: {get_val('index')}
                    Страна: {get_val('country')}
                    Область: {get_val('region')}
                    Район: {get_val('district')}
                    Населенный пункт: {get_val('city')}
                    Улица: {get_val('street')}
                    Дом: {get_val('house')}
                    Строение, корпус: {get_val('building')}
                    Квартира: {get_val('apartment')}

                    Адрес фактического проживания:
                    Индекс: {get_val('index_actual_address')}
                    Страна: {get_val('country_actual_address')}
                    Область: {get_val('region_actual_address')}
                    Район: {get_val('district_actual_address')}
                    Населенный пункт: {get_val('city_actual_address')}
                    Улица: {get_val('street_actual_address')}
                    Дом: {get_val('house_actual_address')}
                    Строение, корпус: {get_val('building_actual_address')}
                    Квартира: {get_val('apartment_actual_address')}

                    Сведения с места работы:
                    Наименование организации: {get_val('organization_name')}
                    Должность: {get_val('position')}
                    Стаж: {get_val('experience')}
                    Доход: {get_val('income')}
                    Телефон отдела кадров или бухгалтерии: {get_val('hr_or_accounting_phone')}

                    Семейное положение, образование, воинская обязанность:
                    Семейное положение: {get_val('marital_status')}
                    Количество иждивенцев: {get_val('number_of_dependents')}
                    Образование: {get_val('education')}
                    Воинская обязанность: {get_val('military_duty')}

                    Данные близкого родственника или супруги/супруга:
                    Фамилия: {get_val('relative_or_spouse_surname')}
                    Имя: {get_val('relative_or_spouse_name')}
                    Отчество: {get_val('relative_or_spouse_patronymic')}
                    Телефон: {get_val('relative_or_spouse_phone')}

                    Фото паспорта:
                    Главный разворот: {get_val('main_passport_spread')}
                    Разворот 30-31: {get_val('spread_30-31')}
                    Разворот с регистрацией: {get_val('spread_with_registration')}
                    """
            }
        }
        response = requests.post(url, json=params)
        result += f"Результат отправки лида в Битрикс24: {response.text}\n"
    return result


