import scrapy

#Scripts\activate เพื่อเข้าไปใน environment 
#ก่อนใช้ ให้เข้าไปใน tutorial ก่อน โดยการ cd tutorial
#ใช้ scrapy crawl quotes -o LMAOXD.csv โดย LMAOXD คือชื่อไฟล์ และ .csv คือนามสกุลที่อยากได้ สามารถเปลี่ยนเป็น json ได้

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://store.steampowered.com/app/551170/Onmyoji/',
        'https://store.steampowered.com/app/1997040/MARVEL_SNAP/',
        'https://store.steampowered.com/app/1811260/EA_SPORTS_FIFA_23/',
        'https://store.steampowered.com/app/1712830/Baldis_Basics_Classic_Remastered/',
        'https://store.steampowered.com/app/493520/GTFO/',
        'https://store.steampowered.com/app/594650/Hunt_Showdown/',
        'https://store.steampowered.com/app/460930/Tom_Clancys_Ghost_Recon_Wildlands/',
        'https://store.steampowered.com/app/1144200/Ready_or_Not/',
        'https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/',
        'https://store.steampowered.com/app/1172470/Apex_Legends/',
        'https://store.steampowered.com/app/440/Team_Fortress_2/',
        'https://store.steampowered.com/app/444090/Paladins/',
        'https://store.steampowered.com/app/359550/Tom_Clancys_Rainbow_Six_Siege/',
        'https://store.steampowered.com/app/1816670/GUNDAM_EVOLUTION/',
        'https://store.steampowered.com/app/261550/Mount__Blade_II_Bannerlord/',
        'https://store.steampowered.com/app/582660/Black_Desert/',
        'https://store.steampowered.com/app/1063730/New_World/',
        'https://store.steampowered.com/app/1172620/Sea_of_Thieves/',
        'https://store.steampowered.com/app/1222680/Need_for_Speed_Heat/',
        'https://store.steampowered.com/app/1551360/Forza_Horizon_5/',
        'https://store.steampowered.com/app/646910/The_Crew_2/',
        'https://store.steampowered.com/app/1687950/Persona_5_Royal/',
        'https://store.steampowered.com/app/1113000/Persona_4_Golden/',
        'https://store.steampowered.com/app/397540/Borderlands_3/',
        'https://store.steampowered.com/app/1217060/Gunfire_Reborn/',
        'https://store.steampowered.com/app/632360/Risk_of_Rain_2/'
    ]

    def parse(self, response):
        for quote in response.css('div.page_content_ctn'):
            yield {
                'url' : response.request.url,
                'title': quote.css('.apphub_AppName::text').get(),
                'tag': quote.css('.app_tag::text').re('Hero Shooter|Battle Royale|Competitive|Roguelite|JRPG|Story Rich|Automobile Sim|Sports|Racing|Driving|Immersive Sim|Tactical|Management|Third Person|Simulation|Co-op|Local Multiplayer|Online Co-Op|PvE|Football|Soccer|PvP|Controller|Team-Based|Realistic|Local Co-Op|Multiplayer|Singleplayer|Anime|Strategy|Card Battler|Casual|PvP|Turn-Based Tactics|Card Game|Deckbuilding|Comic Book|Free to Play|Early Access|Superhero|Stylized|RPG|Free to Play|Turn-Based|Adventure|Fantasy|Stealth|Horror|Action|Parody|Retro|Funny|FPS|Shooter|Open World')
                #'price' : response.selector.xpath('//*[@id="game_area_purchase_section_add_to_cart_389471"]/div[2]/div/div[1]').getall()
            }
            
        next_page = response.css('a.small_cap app_impression_tracked::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

