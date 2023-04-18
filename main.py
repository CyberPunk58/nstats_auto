#Скрипт для выкачивания нужных CSV
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
#Игнорируем устаревший сертификат
options.add_argument('--ignore-certificate-errors')

url = 'https://nstats.bitdotgames.com/stats/resources/83'
#s = Service('/Users/p.andreev/PycharmProjects/nstats_auto/chromedriver_mac/chromedriver')
driver = webdriver.Chrome(chrome_options=options)

driver.get(url=url)
time.sleep(5) #Время для того чтобы открыть страницу со старым сертификатом

#логинимся
email = driver.find_element(By.NAME, "email")
email.send_keys("sofusina")
time.sleep(3)
password = driver.find_element(By.NAME, "password")
password.send_keys("AVactO")
password.send_keys(Keys.ENTER)
time.sleep(5)
#Идем на нужную страницу
#Вводим даты
dateB = '01.03.2023' #Начало периода
dateE = '31.03.2023' #Конец периода
#Создаем массив ресурсов
resource_massive = ['diamonds_paid']
#Создаем массив перфиксов
prefix_massive = ['buy_gold_pack','craft/buy_evolver','craft/buy_evolver','craft/speed_up','craft/upgrade/buy_rating','daily_quest/buy_quest','dungeon','guild_shop/buy_guild_token','guild_shop/buy_reroll','lockbox/open_again/ads_chest','lockbox/open_again/daily_quest','lockbox/open_again/daily1','lockbox/open_again/daily2','lockbox/open_again/daily3','lockbox/open_again/dungeon_stars','lockbox/open_again/guild_shop','shop/buy/market_shop_refresh/class_shop','shop/buy/lockbox/shop_new_lockbox/items_and_abilities/items','lockbox/open_again/shop_new_lockbox/items_and_abilities/items','lockbox/open_again/shop_abil_extracted/magic_items','lockbox/open_again/shop_abil_extracted/melee_items','lockbox/open_again/shop_abil_extracted/ranged_items','shop/buy/lockbox/shop_abil_extracted/magic_items','shop/buy/lockbox/shop_abil_extracted/melee_items','shop/buy/lockbox/shop_abil_extracted/ranged_items','affix_reroll/items','lockbox/open_again/reroll_affix_resource/item_tier_1_3','lockbox/open_again/reroll_affix_resource/item_tier_4_6','lockbox/open_again/reroll_affix_resource/item_tier_7_9','lockbox/open_again/reroll_affix_resource/item_tier_10_12','lockbox/open_again/reroll_affix_resource/item_tier_13_14','lockbox/open_again/reroll_affix_resource/item_tier_15_16','lockbox/open_again/reroll_affix_resource/item_tier_17','lockbox/open_again/reroll_affix_resource/item_tier_18','lockbox/open_again/reroll_affix_resource/item_tier_19','lockbox/open_again/reroll_affix_resource/item_tier_20','ability/buy_evolver','ability/speed_up','arena_shop/buy_reroll','buy_gold_pack','daily_quest/buy_quest','enchant/buy_mana','lockbox/open_again/ability','lockbox/open_again/ads_chest','lockbox/open_again/arena_shop','lockbox/open_again/daily_quest','shop/buy/market_shop_refresh/class_shop','shop/buy/lockbox/shop_new_lockbox/items_and_abilities/abilities','lockbox/open_again/shop_new_lockbox/items_and_abilities/abilities','lockbox/open_again/shop_abil_extracted/magic_abilities','lockbox/open_again/shop_abil_extracted/melee_abilities','lockbox/open_again/shop_abil_extracted/ranged_abilities','shop/buy/lockbox/shop_abil_extracted/magic_abilities','shop/buy/lockbox/shop_abil_extracted/melee_abilities','shop/buy/lockbox/shop_abil_extracted/ranged_abilities','affix_reroll/abilities','lockbox/open_again/reroll_affix_resource/ability_gen_1_2','lockbox/open_again/reroll_affix_resource/ability_gen_3_4','lockbox/open_again/reroll_affix_resource/ability_gen_5_6','lockbox/open_again/reroll_affix_resource/ability_gen_7','lockbox/open_again/reroll_affix_resource/ability_gen_8','lockbox/open_again/reroll_affix_resource/ability_gen_9','lockbox/open_again/reroll_affix_resource/ability_gen_10','lockbox/open_again/reroll_affix_resource/ability_gen_11','shop/buy/lockbox/rune/rune_gold','shop/buy/lockbox/rune/rune_legendary','shop/buy/lockbox/rune/rune_silver','lockbox/open_again/pet','lockbox/open_again/pet_shop/armor','lockbox/open_again/pet_treasure','pets/buy_evolver','pets/item_upgrade','pets/pet_energy','pets/spirits_hunting_attempts','pets/treasure_search_attempts','shop/buy/lockbox/pet_shop','shop/buy/lockbox/pet_shop/armor','event/mini_events','lockbox/open_again/event/mini_events','event/battle_passes/newbies','event/holidays','lockbox/open_again/event/holidays','tamagotchi','offers']
#Для выбора платформы, но пока не трогаем
platform_massive = ['55']
#Создаем нужную ссылку для андроида в цикле, по массиву ресурсов
for pref in range(0, len(prefix_massive)):
    new_url = "http://nstats.bitdotgames.com/stats/resources/55?bday="+ dateB + "&eday=" + dateE + "&resource=" + resource_massive[0] + "&eprefix=" + prefix_massive[pref]
    driver.get(new_url)
    time.sleep(5)
    clickCSV = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/button").click()
    time.sleep(1)
    downloadCSV = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/ul/li[1]/a").click()
    time.sleep(5)

driver.close()
driver.quit()