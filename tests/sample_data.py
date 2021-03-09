SAMPLE_STATUS_EN = {
    "lang": "en_US",
    "categories": [
        {"name": "Wii U", "type": 0},
        {"name": "nintendo 3DS", "type": 0},
        {"name": "Wii", "type": 0},
        {"name": "nintendo DS", "type": 0},
        {"name": "web", "type": 0},
        {"name": "other", "type": 0},
        {"name": "iOS", "type": 0},
        {"name": "Nintendo Switch", "type": 0},
        {"name": "Android", "type": 0},
    ],
    "operational_statuses": [
        {
            "platform": ["web"],
            "platform_image": ["img/label_web.png"],
            "software_title": "Purchasing on Nintendo Game Store",
            "message": "During the times specified below, ... \nAt this time, the network service is back up and...",
            "free_write": "",
            "begin": "Monday, January 22, 2018  2 :14 AM",
            "end": "Monday, January 22, 2018  3 :07 AM",
            "utc_del_time": "2018-01-23 03:07:00",
            "event_status": "0",
            "services": ["All network services"],
            "update_date": "Monday, January 22, 2018",
        }
    ],
    "temporary_maintenances": [
        {
            "platform": ["Nintendo Switch"],
            "platform_image": ["img/label_switch.png"],
            "software_title": "Online play of some software",
            "message": "Server maintenance has been completed. Thank you for your cooperation.",
            "free_write": "",
            "begin": "Wednesday, February 24, 2021  6 :55 AM",
            "end": "Wednesday, February 24, 2021  7 :01 AM",
            "utc_del_time": "2021-02-25 15:01:00",
            "event_status": "3",
            "services": ["certain network services"],
            "update_date": "Wednesday, February 24, 2021",
        },
        {
            "platform": ["Nintendo Switch"],
            "platform_image": ["img/label_switch.png"],
            "software_title": "Network Services",
            "message": "During the maintenance window, network services may be unavailable.",
            "free_write": "",
            "begin": "Wednesday, February 24, 2021  8 :30 PM",
            "end": "Wednesday, February 24, 2021 11 :30 PM",
            "event_status": "0",
            "services": ["Notice to friends, etc."],
            "update_date": "Tuesday, February 23, 2021",
        },
    ],
}


SAMPLE_STATUS_DE = {
    "lang": "de_DE",
    "categories": [
        {"name": "Wii U", "type": 0},
        {"name": "nintendo 3DS", "type": 0},
        {"name": "Wii", "type": 0},
        {"name": "nintendo DS", "type": 0},
        {"name": "web", "type": 0},
        {"name": "other", "type": 0},
        {"name": "iOS", "type": 0},
        {"name": "Nintendo Switch", "type": 0},
        {"name": "Android", "type": 0},
    ],
    "operational_statuses": [
        {
            "platform": ["web"],
            "platform_image": ["img/label_web.png"],
            "software_title": "Kauf im Nintendo Game Store",
            "message": "Während der unten angegebenen Zeiten... \nZu diesem Zeitpunkt ist der Netzwerkdienst wieder...",
            "free_write": "",
            "begin": "Montag, 22. Januar 2018, 11:14 Bin",
            "end": "Montag, 22. Januar 2018, 12:07 Uhr",
            "utc_del_time": "2018-01-23 03:07:00",
            "event_status": "0",
            "services": ["Alle Netzwerkdienste"],
            "update_date": "Montag, 22. Januar 2018",
        }
    ],
    "temporary_maintenances": [
        {
            "platform": ["Nintendo Switch"],
            "platform_image": ["img/label_switch.png"],
            "software_title": "Online-Spiel für einige Software-Titel",
            "message": "Die Wartungsarbeiten am Server sind abgeschlossen. Vielen Dank für deine Geduld.",
            "free_write": "",
            "begin": "Mittwoch, 24. Februar 2021, 15:55 Uhr",
            "end": "Mittwoch, 24. Februar 2021, 16:01 Uhr",
            "utc_del_time": "2021-02-25 15:01:00",
            "event_status": "3",
            "services": ["bestimmte Netzdienste"],
            "update_date": "Mittwoch, 24. Februar 2021",
        },
        {
            "platform": ["Nintendo Switch"],
            "platform_image": ["img/label_switch.png"],
            "software_title": "Online-Services",
            "message": "Während des angegebenen Zeitraums führen wir Wartungsarbeiten am Server durch...",
            "free_write": "",
            "begin": "Donnerstag, 25. Februar 2021,  5:30 Uhr",
            "end": "Donnerstag, 25. Februar 2021,  8:30 Uhr",
            "event_status": "0",
            "services": ["Freundesmitteilungen, etc."],
            "update_date": "Mittwoch, 24. Februar 2021",
        },
    ],
}

SAMPLE_GAME = {
    "content_type": "title",
    "dominant_colors": ["0c1016", "fafaf9", "fce862"],
    "formal_name": "Among Us",
    "hero_banner_url": "https://example.com/hero.jpg",
    "id": 70010000036098,
    "is_new": False,
    "membership_required": False,
    "public_status": "public",
    "rating_info": {
        "content_descriptors": [
            {
                "id": 14,
                "name": "Fantasy Violence",
                "type": "descriptor",
                "image_url": "https://example.com/foo.jpg",
                "svg_image_url": "https://example.com/foo.svg",
            },
            {
                "id": 31,
                "name": "Mild Blood",
                "type": "descriptor",
                "image_url": "https://example.com/bar.jpg",
                "svg_image_url": "https://example.com/bar.svg",
            },
        ],
        "rating": {
            "age": 10,
            "id": 3,
            "image_url": "https://example.com/e10.jpg",
            "name": "E10+",
            "provisional": False,
            "svg_image_url": "https://example.com/e10.svg",
        },
        "rating_system": {"id": 202, "name": "ESRB"},
    },
    "release_date_on_eshop": "2020-12-15",
    "screenshots": [
        {"images": [{"url": "https://example.com/1.jpg"}]},
        {"images": [{"url": "https://example.com/2.jpg"}]},
    ],
    "tags": [],
    "target_titles": [],
}

SAMPLE_PRICE_RESPONSE  ={
    "personalized": False,
    "country": "US",
    "prices": [
        {
            "title_id": 70010000039205,
            "sales_status": "onsale",
            "regular_price": {"amount": "$3.99", "currency": "USD", "raw_value": "3.99"},
            "discount_price": {
                "amount": "$2.99",
                "currency": "USD",
                "raw_value": "2.99",
                "start_datetime": "2021-03-06T10:00:00Z",
                "end_datetime": "2021-03-26T15:59:59Z",
            },
        }
    ],
}