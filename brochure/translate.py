#!/usr/bin/env python3
"""Generate Cantonese (Traditional Chinese, HK) versions of both brochures."""
from pathlib import Path

# Translation map - English -> Traditional Chinese (HK style).
# LONGEST/MOST-SPECIFIC FIRST so they match before generic words.

TRANSLATIONS = [
    # === Full sentences / paragraphs ===
    ("Thank you for the trust placed in Pangea Properties. Following our conversations\n          about your principal's brief — a <b>2–3 bedroom residence near the Burj Khalifa,\n          at AED 8 million</b>, ready for use during his annual visits to Dubai — I've\n          prepared this brochure for the residence I believe most closely matches what\n          he is looking for.",
     "感謝您對 Pangea Properties 的信任。根據您客戶的要求 — <b>位於哈里發塔附近的 2-3 房單位，預算 AED 800 萬</b>，作為其每年到訪杜拜的住所 — 本人特此為您準備此份介紹，相信此單位最切合其需要。"),
    ("Thank you for the trust placed in Pangea Properties. Following our conversations\n      about your principal's brief — a <b>2–3 bedroom residence near the Burj Khalifa,\n      at AED 8 million</b>, ready for use during his annual visits to Dubai — I've\n      prepared this brochure for the residence I believe most closely matches what he\n      is looking for.",
     "感謝您對 Pangea Properties 的信任。根據您客戶的要求 — <b>位於哈里發塔附近的 2-3 房單位，預算 AED 800 萬</b>，作為其每年到訪杜拜的住所 — 本人特此為您準備此份介紹，相信此單位最切合其需要。"),
    ("Vida Dubai Mall · Tower 1 is a <b>brand-new, fully furnished</b> serviced\n          residence by Emaar. It is the <b>largest 3-bedroom layout</b> in the building,\n          high above Downtown on the <b>23<sup>rd</sup> floor</b>, with floor-to-ceiling\n          views of the Burj Khalifa and the Dubai Fountain — a travel-and-live home\n          that requires no setup on arrival.",
     "Vida Dubai Mall · 一號塔為 Emaar 旗下<b>全新落成、全套傢俬電器配備</b>的服務式住宅。本單位為大廈內<b>最大三房間隔</b>，位於市中心高層 <b>23 樓</b>，落地玻璃盡覽哈里發塔及杜拜噴泉景觀 — 是即住即用、無需任何佈置的旅居之選。"),
    ("Vida Dubai Mall · Tower 1 is a <b>brand-new, fully furnished</b> serviced residence by\n      Emaar. It is the <b>largest 3-bedroom layout</b> in the building, high above Downtown\n      on the <b>23<sup>rd</sup> floor</b>, with floor-to-ceiling views of the Burj Khalifa\n      and the Dubai Fountain — a travel-and-live home that requires no setup on arrival.",
     "Vida Dubai Mall · 一號塔為 Emaar 旗下<b>全新落成、全套傢俬電器配備</b>的服務式住宅。本單位為大廈內<b>最大三房間隔</b>，位於市中心高層 <b>23 樓</b>，落地玻璃盡覽哈里發塔及杜拜噴泉景觀 — 是即住即用、無需任何佈置的旅居之選。"),
    ("Vida Dubai Mall is the residential expression of Emaar's <b>Vida Hotels &amp;\n          Resorts</b> brand — a <b>238-metre, 55-storey tower</b> at the heart of Downtown\n          Dubai, anchored by the 195-key Vida Dubai Mall hotel.",
     "Vida Dubai Mall 為 Emaar 旗下 <b>Vida Hotels &amp; Resorts</b> 品牌的住宅版本 — 一座位於杜拜市中心的 <b>238 米、55 層大廈</b>，內設 195 間客房的 Vida 酒店。"),
    ("Vida Dubai Mall is the residential expression of Emaar's <b>Vida Hotels &amp; Resorts</b>\n      brand — a <b>238-metre, 55-storey tower</b> at the heart of Downtown Dubai, anchored\n      by the 195-key Vida Dubai Mall hotel.",
     "Vida Dubai Mall 為 Emaar 旗下 <b>Vida Hotels &amp; Resorts</b> 品牌的住宅版本 — 一座位於杜拜市中心的 <b>238 米、55 層大廈</b>，內設 195 間客房的 Vida 酒店。"),
    ("Tower 1 is the original tower, and the only residential address in Downtown\n          <b>connected directly</b> to The Dubai Mall by a private, air-conditioned sky-bridge.",
     "一號塔為首座建成的塔樓，亦是杜拜市中心唯一<b>直接連接</b>杜拜購物中心的住宅地址，由私人冷氣天橋連通。"),
    ("Tower 1 is the original tower, and the only residential address in Downtown\n      <b>connected directly</b> to The Dubai Mall by a private, air-conditioned sky-bridge.",
     "一號塔為首座建成的塔樓，亦是杜拜市中心唯一<b>直接連接</b>杜拜購物中心的住宅地址，由私人冷氣天橋連通。"),
    ("This residence sits on a confirmed <b>Burj Khalifa &amp; Dubai Fountain stack</b> — the\n      most sought-after view orientation in the building. The <b>main balcony</b> stretches\n      from the drawing room to the master bedroom, framing the Burj head-on with the Fountain\n      promenade and Downtown skyline filling the horizon.",
     "本單位確定位於 <b>哈里發塔及杜拜噴泉景觀軸線</b> — 大廈內最搶手的景觀方向。<b>主露台</b>由客廳延伸至主人睡房，正面飽覽哈里發塔，配合噴泉長廊及市中心天際線盡收眼底。"),
    ("This residence sits on a confirmed <b>Burj Khalifa &amp; Dubai Fountain stack</b> — the\n          most sought-after view orientation in the building. The <b>main balcony</b> stretches\n          from the drawing room to the master bedroom, framing the Burj head-on with the\n          Fountain promenade and Downtown skyline filling the horizon.",
     "本單位確定位於 <b>哈里發塔及杜拜噴泉景觀軸線</b> — 大廈內最搶手的景觀方向。<b>主露台</b>由客廳延伸至主人睡房，正面飽覽哈里發塔，配合噴泉長廊及市中心天際線盡收眼底。"),
    ("Step out of the lobby and you're inside The Dubai Mall in roughly three minutes — without\n      crossing a road or stepping into the heat.",
     "從大堂出發約三分鐘即可進入杜拜購物中心 — 無需過馬路、無需頂著酷暑。"),
    ("Step out of the lobby and you're inside The Dubai Mall in roughly three minutes —\n      without crossing a road or stepping into the heat.",
     "從大堂出發約三分鐘即可進入杜拜購物中心 — 無需過馬路、無需頂著酷暑。"),
    ("This single feature is the <b>most-cited reason</b> residents and short-stay guests choose\n      this building over any other Downtown address.",
     "此項配套是住戶及短期入住者選擇本大廈而非其他市中心地址的<b>最常見原因</b>。"),
    ("<b>Private, air-conditioned sky-bridge</b> — residents and hotel guests only.",
     "<b>私人冷氣天橋</b> — 僅限住戶及酒店客人使用。"),
    ("<b>200+ F&amp;B outlets</b> and the Dubai Aquarium, all reachable on foot.",
     "<b>逾 200 間餐飲</b>及杜拜水族館，全部步行可達。"),
    ("Direct access to The Dubai Fountain promenade and Burj Park.",
     "直達杜拜噴泉長廊及哈里發塔公園。"),
    ("An <b>outdoor temperature-controlled pool</b> with full Downtown skyline frontage — a working pool\n      for residents, distinct from the hotel guest pool. Sun loungers, cabana seating, and direct\n      service from the lobby café.",
     "<b>戶外恆溫泳池</b>，正面飽覽市中心天際線 — 為住戶設置的實用型泳池，與酒店客人專用泳池分開。設有日光浴床、私人涼亭座位，並由大堂咖啡廳直接送餐。"),
    ("Outdoor temperature-controlled pool with full Downtown skyline frontage — a working pool for\n      residents, distinct from the hotel guest pool.",
     "戶外恆溫泳池，正面飽覽市中心天際線 — 為住戶設置的實用型泳池，與酒店客人專用泳池分開。"),
    ("A double-height lobby with signature pendant lighting, a curated art programme, and a café\n      that opens onto the pool deck.",
     "雙層挑高大堂，配以標誌性吊燈、精選藝術品展示，並設有通往泳池平台的咖啡廳。"),
    ("A double-height lobby with signature pendant lighting, a curated art programme,\n      and a café that opens onto the pool deck.",
     "雙層挑高大堂，配以標誌性吊燈、精選藝術品展示，並設有通往泳池平台的咖啡廳。"),
    ("Residents have access to multiple lounge spaces throughout the day — a <b>daylight lounge</b> with\n      Burj views off the lobby, an evening <b>reading and cocktail lounge</b> with library, and a\n      double-height <b>atrium lounge</b> anchored by a curated art installation. All three are\n      residents-and-hotel-guests only — no public access.",
     "住戶全日可使用多個休憩空間 — 大堂旁設有<b>日光休憩廳</b>飽覽哈里發塔，晚間設有<b>閱讀及雞尾酒休憩廳</b>，以及雙層挑高、由藝術裝置點綴的<b>中庭休憩廳</b>。三個休憩廳僅限住戶及酒店客人使用 — 不對外開放。"),
    ("Origins is the building's signature restaurant — <b>all-day dining</b> with a buffet counter\n      and à-la-carte service.",
     "Origins 為大廈內的標誌性餐廳 — <b>全日供餐</b>，設有自助餐區及單點服務。"),
    ("Beyond Origins, residents have direct in-building access to a chic <b>lobby café</b> and the\n      hotel's <b>evening cocktail lounge</b>, plus 200+ F&amp;B outlets inside The Dubai Mall via\n      the sky-bridge.",
     "除 Origins 外，住戶可直接使用<b>大堂咖啡廳</b>及酒店的<b>晚間雞尾酒酒廊</b>，並可經天橋使用杜拜購物中心內逾 200 間餐飲。"),
    ("All-day dining with a buffet counter and à-la-carte service. Plus a chic lobby café,\n      evening cocktail lounge and 200+ F&amp;B outlets inside The Dubai Mall via the sky-bridge.",
     "全日供餐，設有自助餐區及單點服務。另設大堂咖啡廳、晚間雞尾酒酒廊，並可經天橋使用杜拜購物中心內逾 200 間餐飲。"),
    ("A <b>24-hour fitness centre</b> with full Matrix-equipped cardio and resistance training,\n      alongside the Vida-branded <b>spa</b> offering tailored treatments, sauna, steam room, and\n      sun terraces — all available to residents under the Vida hotel programme.",
     "<b>24 小時健身中心</b>，配備全套 Matrix 心肺及阻力訓練器材，並設 Vida 品牌<b>水療中心</b>提供度身定制療程、桑拿、蒸氣浴及日光露台 — 住戶可使用 Vida 酒店全部設施。"),
    ("24-hour fitness centre with Matrix-equipped cardio and resistance training, plus the\n      Vida-branded spa offering tailored treatments, sauna, steam and sun terraces.",
     "24 小時健身中心配備 Matrix 心肺及阻力訓練器材，並設 Vida 品牌水療中心提供度身定制療程、桑拿、蒸氣及日光露台。"),
    ("<b>Qix Club</b> is the supervised kids' club for ages 4–12 — indoor play, an outdoor activity deck\n      and structured weekly programmes. For the adults, a dedicated <b>co-working floor</b> offers Mac\n      stations, private booths and a fireplaced lounge — designed for residents who work from home a\n      few days a week.",
     "<b>Qix 兒童俱樂部</b>為 4-12 歲兒童提供有監督的活動 — 室內遊戲、戶外活動平台及每週主題節目。為大人而設的<b>共享工作層</b>則配備 Mac 工作站、私人會議廂及壁爐休憩廳 — 適合每週在家工作數天的住戶。"),
    ("Five sunlit meeting rooms accommodate up to <b>156 guests</b> across boardroom, banquet and\n      theatre layouts. A function terrace and event deck extend the offer for private parties,\n      weddings and corporate offsites — <b>a meaningful amenity</b> for residents using the property\n      for both home and entertaining.",
     "五間採光充足的會議室，可容納 <b>156 位來賓</b>，提供董事會、宴會及劇院式佈局。另設活動露台及活動平台，可舉辦私人聚會、婚宴及企業活動 — 對於同時用作居住及接待的住戶來說<b>是難得的配套</b>。"),
    ("The amenities programme is the same one operated for the Vida hotel — residents have full\n          access under the building's <b>branded service</b> contract.",
     "本設施由 Vida 酒店團隊統一管理 — 住戶可於大廈<b>品牌服務合約</b>下全面使用。"),
    ("The master suite <b>faces the Burj head-on</b>, with a private balcony door, walk-in dressing area\n      and an ensuite bathroom with both a soaking tub and a separate rain shower.",
     "主人套房<b>正面望向哈里發塔</b>，設有私人露台門、步入式更衣間，以及配備浸浴缸和獨立花灑間的套房浴室。"),
    ("The residence runs the full depth of the tower, with <b>two distinct outlooks</b>. The\n      main balcony — accessed from the drawing room and stretching the length of the master\n      bedroom — frames the Burj Khalifa. This second balcony, off the additional bedroom,\n      looks the opposite way across <b>DIFC</b> and Sheikh Zayed Road.",
     "本單位橫跨整個塔樓深度，擁有<b>兩個不同景觀</b>。主露台由客廳出入，延伸至主人睡房，正面望向哈里發塔。第二露台則由額外睡房出入，向相反方向望出，飽覽 <b>DIFC</b> 及謝赫扎耶德大道。"),
    ("The residence runs the full depth of the tower, with <b>two distinct outlooks</b>. The main balcony\n      (drawing room → master bedroom) frames the Burj Khalifa. This second balcony, off the additional\n      bedroom, looks the opposite way across <b>DIFC</b> and Sheikh Zayed Road.",
     "本單位橫跨整個塔樓深度，擁有<b>兩個不同景觀</b>。主露台（客廳至主人睡房）正面望向哈里發塔。第二露台則由額外睡房出入，向相反方向望出，飽覽 <b>DIFC</b> 及謝赫扎耶德大道。"),
    ("The unit is available for viewing. I'd suggest doing this at the <b>golden hour</b> so the Burj\n      and Fountain show at their best, paired with a short walk across the sky-bridge into The\n      Dubai Mall to feel the location difference firsthand.",
     "本單位可供視察。建議於<b>黃金時段</b>視察，可欣賞哈里發塔及噴泉的最佳狀態，並可步行經天橋進入杜拜購物中心，親身感受位置之便利。"),
    ("The unit is available for viewing. I'd suggest doing this at the <b>golden hour</b> so the Burj\n      and Fountain show at their best, paired with a short walk across the sky-bridge into The Dubai\n      Mall to feel the location difference firsthand. The buying process typically runs\n      <b>4–6 weeks</b> from MOU to transfer.",
     "本單位可供視察。建議於<b>黃金時段</b>視察，可欣賞哈里發塔及噴泉的最佳狀態，並可步行經天橋進入杜拜購物中心，親身感受位置之便利。本大廈成屋單位之購買程序由 MOU 至轉名通常為 <b>4-6 週</b>。"),
    ("The buying process for a ready unit in this building typically runs <b>4–6 weeks</b> from MOU\n      to transfer.",
     "本大廈成屋單位之購買程序由 MOU 至轉名通常為 <b>4-6 週</b>。"),
    ("Building exterior and lifestyle renders are extracted from the Emaar Vida Dubai Mall developer\n      brochure. Building amenity photography is the property of Vida Hotels &amp; Resorts / Emaar\n      Hospitality. Unit photography is sourced from the Pangea Properties listing. Final commercial\n      terms are subject to confirmation against the title deed and RERA Form F.",
     "大廈外觀及生活效果圖取自 Emaar Vida Dubai Mall 發展商小冊子。大廈設施相片版權屬於 Vida Hotels &amp; Resorts / Emaar Hospitality。單位相片來自 Pangea Properties 上盤資料。最終商業條款須以樓契及 RERA F 表為準。"),
    ("Building exterior and lifestyle renders extracted from the Emaar Vida Dubai Mall developer\n      brochure. Building amenity photography is property of Vida Hotels &amp; Resorts / Emaar\n      Hospitality. Unit photography sourced from the Pangea Properties listing. Final commercial\n      terms subject to confirmation against the title deed and RERA Form F.",
     "大廈外觀及生活效果圖取自 Emaar Vida Dubai Mall 發展商小冊子。大廈設施相片版權屬於 Vida Hotels &amp; Resorts / Emaar Hospitality。單位相片來自 Pangea Properties 上盤資料。最終商業條款須以樓契及 RERA F 表為準。"),

    # === Personal note specifics ===
    (">\n          To\n        </div>", ">\n          致\n        </div>"),  # landscape
    (">To</div>", ">致</div>"),  # portrait
    ("Prepared for Mr. Xie Xingyao · Hong Kong", "致 謝興堯先生 · 香港"),
    ("For Mr. Xie Xingyao · HK", "致 謝先生 · 香港"),
    ("Personal Note &nbsp;·&nbsp; Prepared 24 May 2026", "個人信函 &nbsp;·&nbsp; 2026 年 5 月 24 日"),
    ("Personal Note &nbsp;·&nbsp; 24 May 2026", "個人信函 &nbsp;·&nbsp; 2026 年 5 月 24 日"),
    ('Hong Kong &nbsp;·&nbsp; On behalf of your principal', "香港 &nbsp;·&nbsp; 代表您的客戶"),
    ('Mr. <b style="font-weight:700;">Xie Xingyao</b>', '<b style="font-weight:700;">謝興堯</b> 先生'),
    ("Dear Mr. Xie,", "謝先生 您好，"),

    # === Cover taglines (must come BEFORE generic "Burj Khalifa") ===
    ("Full Burj Khalifa &amp; Fountain view &nbsp;·&nbsp; Maid's room &nbsp;·&nbsp; Ready &amp; Furnished",
     "全景哈里發塔及噴泉景觀 &nbsp;·&nbsp; 設工人房 &nbsp;·&nbsp; 即住 · 配備齊全"),
    ("Full Burj Khalifa &amp; Fountain view<br/>Maid's room &nbsp;·&nbsp; Ready &amp; Furnished",
     "全景哈里發塔及噴泉景觀<br/>設工人房 &nbsp;·&nbsp; 即住 · 配備齊全"),

    # === Why-this-matches matrix ===
    ("Why this residence matches the brief", "此單位契合客戶要求的原因"),
    ("Fully furnished &amp; serviced by Vida — arrive with a suitcase, leave with a suitcase. No decoration or setup required.",
     "Vida 服務式管理，全套傢俬電器配備 — 帶一個行李箱即可入住，無需任何裝修或佈置。"),
    ("Fully furnished &amp; serviced by Vida — arrive with a suitcase, leave with a suitcase. No decoration required.",
     "Vida 服務式管理，全套傢俬電器配備 — 帶一個行李箱即可入住，無需任何佈置。"),
    ("Fully furnished &amp; serviced by Vida — arrive with a suitcase, leave with a suitcase.",
     "Vida 服務式管理，全套傢俬電器配備 — 帶一個行李箱即可入住。"),
    ("Confirmed Burj &amp; Fountain stack — head-on views from the master bedroom and the panoramic balcony.",
     "確認位於哈里發塔及噴泉景觀軸線 — 主人睡房及全景露台正面望塔。"),
    ("Confirmed Burj &amp; Fountain stack — head-on from the master bedroom and the panoramic balcony.",
     "確認位於哈里發塔及噴泉景觀軸線 — 主人睡房及全景露台正面望塔。"),
    ("23<sup>rd</sup> floor — high above the boulevard for night views and the cleaner air your principal prefers.",
     "23 樓 — 高於大街景觀，可賞夜景及享空氣清新環境。"),
    ("23<sup>rd</sup> floor — night views and the cleaner air your principal prefers.",
     "23 樓 — 飽覽夜景，並享空氣清新環境。"),
    ("23<sup>rd</sup> floor — high above the boulevard for night views of the Burj and the cleaner air your principal prefers.",
     "23 樓 — 高於大街景觀，可賞哈里發塔夜景及享空氣清新環境。"),
    ("On the main boulevard, with a private air-conditioned sky-bridge into The Dubai Mall and direct metro access via the mall.",
     "位處主大街，設有私人冷氣天橋直通杜拜購物中心，並可經商場直達地鐵站。"),
    ("Private air-conditioned sky-bridge into The Dubai Mall and direct metro access.",
     "私人冷氣天橋直通杜拜購物中心，並可直達地鐵站。"),
    ("2 covered parking bays · 4 elevators in the tower — short, private journeys from car to apartment.",
     "2 個有蓋車位 · 大廈設 4 部升降機 — 由停車場到單位短捷私密。"),
    ("2 covered bays · 4 elevators in the tower.",
     "2 個有蓋車位 · 大廈設 4 部升降機。"),
    ("24/7 gym, Vida spa, residents' lounges, in-house dining at Origins and the kids' Qix Club — all on-site for visiting family.",
     "24 小時健身房、Vida 水療、住戶休憩廳、Origins 樓內餐廳及 Qix 兒童俱樂部 — 訪港家庭一應俱全。"),
    ("24/7 gym, Vida spa, residents' lounges, in-house dining at Origins, Qix Club.",
     "24 小時健身房、Vida 水療、住戶休憩廳、Origins 餐廳及 Qix 兒童俱樂部。"),

    # === Eyebrow ===
    ("Property Brochure &nbsp;·&nbsp; Downtown Dubai", "物業簡介 &nbsp;·&nbsp; 杜拜市中心"),

    # === H2 / display titles ===
    ("A gateway into a<br/><b>thriving city.</b>", "通往繁華都會<br/>的<b>門戶。</b>"),
    ("Seamlessly connected to<br/><b>The Dubai Mall.</b>", "無縫連接<br/><b>杜拜購物中心。</b>"),
    ("Seamlessly connected<br/>to <b>The Dubai Mall.</b>", "無縫連接<br/><b>杜拜購物中心。</b>"),
    ('Burj Khalifa<br/>at the <b style="font-weight:700;">waterline</b>.',
     '哈里發塔倒映<br/><b style="font-weight:700;">於泳池</b>。'),
    ("Burj Khalifa at the<br/><b>waterline</b>.", "哈里發塔倒映<br/><b>於泳池</b>。"),
    ("Two angles,<br/><b>one skyline.</b>", "兩個角度，<br/><b>同一天際線。</b>"),
    ("The <b>arrival</b><br/>sequence.", "<b>入門</b><br/>初印象。"),
    ("Three lounges,<br/><b>three moods.</b>", "三個休憩廳，<br/><b>三種氛圍。</b>"),
    ("<b>Origins</b><br/>the in-house restaurant.", "<b>Origins</b><br/>樓內餐廳。"),
    ("<b>Gym</b>, spa,<br/>sauna &amp; steam.", "<b>健身房</b>、水療、<br/>桑拿及蒸氣浴。"),
    ("Qix Club and the<br/><b>co-working floor.</b>", "Qix 兒童俱樂部及<br/><b>共享工作層。</b>"),
    ("Qix Club &amp; the<br/><b>co-working floor.</b>", "Qix 兒童俱樂部及<br/><b>共享工作層。</b>"),
    ("Five meeting rooms<br/><b>for up to 156.</b>", "五間會議室，<br/><b>可容納 156 人。</b>"),
    ("Five meeting rooms,<br/><b>up to 156 guests.</b>", "五間會議室，<br/><b>可容納 156 人。</b>"),
    ("A full <b>resort floor</b>,<br/>open to residents.", "完整<b>度假式設施層</b>，<br/>住戶專享。"),
    ("Three bedrooms.<br/>Burj-facing. <b>Ready.</b>", "三房單位 · 望哈里發塔<br/><b>即住。</b>"),
    ("The <b>reception</b><br/>areas.", "主要<br/><b>起居空間。</b>"),
    ("Open-plan,<br/><b>balcony-out.</b>", "開放式佈局，<br/><b>露台景觀。</b>"),
    ("<b>Fully fitted.</b><br/>Floor-to-ceiling.", "<b>全套配備。</b><br/>落地玻璃。"),
    ("The <b>panoramic balcony</b>,<br/>front-row to Downtown.", "<b>全景露台</b>，<br/>市中心第一排。"),
    ("<b>Wake up</b><br/>to the Burj.", "伴<b>哈里發塔</b><br/>醒來。"),
    ("The <b>master</b><br/>bathroom.", "<b>主人</b><br/>浴室。"),
    ("<b>Two further</b><br/>bedrooms.", "另設<br/><b>兩間客房。</b>"),
    ("Maid's room<br/><b>and the wider view.</b>", "工人房<br/><b>及更廣景觀。</b>"),
    ("Maid's room<br/><b>&amp; powder room.</b>", "工人房及<br/><b>客用洗手間。</b>"),
    ("A <b>second view</b>,<br/>across the DIFC skyline.", "另一<b>景觀</b>，<br/>飽覽 DIFC 天際線。"),
    ("The <b>detail.</b>", "<b>詳細資料。</b>"),
    ("Let's arrange<br/>a <b>viewing.</b>", "誠邀您安排<br/><b>實地視察。</b>"),

    # === Section labels (numbered) ===
    ("01 &nbsp;·&nbsp; The Building", "01 &nbsp;·&nbsp; 大廈介紹"),
    ("02 &nbsp;·&nbsp; The View", "02 &nbsp;·&nbsp; 景觀"),
    ("03 &nbsp;·&nbsp; Connected", "03 &nbsp;·&nbsp; 交通連繫"),
    ("04 &nbsp;·&nbsp; The Pool, cont.", "04 &nbsp;·&nbsp; 泳池（續）"),
    ("04 &nbsp;·&nbsp; The Pool", "04 &nbsp;·&nbsp; 泳池"),
    ("05 &nbsp;·&nbsp; Lobby &amp; Lounges", "05 &nbsp;·&nbsp; 大堂及休憩廳"),
    ("05 &nbsp;·&nbsp; Lobby", "05 &nbsp;·&nbsp; 大堂"),
    ("06 &nbsp;·&nbsp; Residents' Lounges", "06 &nbsp;·&nbsp; 住戶休憩廳"),
    ("07 &nbsp;·&nbsp; Dining", "07 &nbsp;·&nbsp; 餐飲"),
    ("08 &nbsp;·&nbsp; Wellness", "08 &nbsp;·&nbsp; 健康設施"),
    ("09 &nbsp;·&nbsp; Family &amp; Work", "09 &nbsp;·&nbsp; 親子與工作"),
    ("10 &nbsp;·&nbsp; Meeting &amp; Events", "10 &nbsp;·&nbsp; 會議及活動"),
    ("10 &nbsp;·&nbsp; Meetings &amp; Events", "10 &nbsp;·&nbsp; 會議及活動"),
    ("11 &nbsp;·&nbsp; Amenities", "11 &nbsp;·&nbsp; 會所設施"),
    ("11 &nbsp;·&nbsp; The Residence", "11 &nbsp;·&nbsp; 單位介紹"),
    ("12 &nbsp;·&nbsp; The Residence", "12 &nbsp;·&nbsp; 單位介紹"),
    ("12 &nbsp;·&nbsp; Living &amp; Dining, cont.", "12 &nbsp;·&nbsp; 客廳與飯廳（續）"),
    ("12 &nbsp;·&nbsp; Living &amp; Dining", "12 &nbsp;·&nbsp; 客廳與飯廳"),
    ("13 &nbsp;·&nbsp; Kitchen &amp; Balcony", "13 &nbsp;·&nbsp; 廚房及露台"),
    ("13 &nbsp;·&nbsp; The Balcony", "13 &nbsp;·&nbsp; 露台"),
    ("14 &nbsp;·&nbsp; Master Bedroom", "14 &nbsp;·&nbsp; 主人睡房"),
    ("15 &nbsp;·&nbsp; Master Ensuite", "15 &nbsp;·&nbsp; 主人浴室"),
    ("16 &nbsp;·&nbsp; Guest Bedrooms", "16 &nbsp;·&nbsp; 客房"),
    ("17 &nbsp;·&nbsp; The Second Balcony", "17 &nbsp;·&nbsp; 第二露台"),
    ("17 &nbsp;·&nbsp; Additional", "17 &nbsp;·&nbsp; 其他空間"),
    ("17 &nbsp;·&nbsp; Specifications", "18 &nbsp;·&nbsp; 規格"),
    ("18 &nbsp;·&nbsp; Specifications", "18 &nbsp;·&nbsp; 規格"),
    ("18 &nbsp;·&nbsp; Next Steps", "19 &nbsp;·&nbsp; 下一步"),

    # === Captions, labels ===
    ("Outdoor Pool Deck · Full Burj Khalifa Frontage", "戶外泳池平台 · 正面望哈里發塔"),
    ("Hotel Lobby · Double-Height Ceiling &amp; Signature Pendant Lighting",
     "酒店大堂 · 雙層挑高天花及標誌性吊燈"),
    ("Pool toward Burj &amp; Emaar Square", "泳池望向哈里發塔及 Emaar 廣場"),
    ("Pool deck &amp; lounge seating", "泳池平台及休憩座位"),
    ("Daylight Lounge · Burj View", "日光休憩廳 · 望哈里發塔"),
    ("Evening Library Lounge", "晚間圖書館休憩廳"),
    ("Atrium Lounge · Art Wall", "中庭休憩廳 · 藝術牆"),
    ("Off the lobby, with full Burj views and a café.", "大堂旁，全景望哈里發塔，並設咖啡廳。"),
    ("Evening reading &amp; cocktail lounge with a library wall.", "晚間閱讀及雞尾酒休憩廳，配藏書牆。"),
    ("Double-height lounge anchored by a curated art installation.", "雙層挑高休憩廳，以精選藝術裝置為主軸。"),
    ("24/7 Fitness Centre · Matrix Equipment", "24 小時健身中心 · Matrix 器材"),
    ("Vida Spa · Treatment Room", "Vida 水療 · 療程室"),
    ("Qix Club · Indoor Play Deck", "Qix 俱樂部 · 室內遊戲區"),
    ("Qix Club · Indoor Play", "Qix 俱樂部 · 室內遊戲"),
    ("Outdoor Play Deck", "戶外遊戲平台"),
    ("Co-Working Space", "共享工作空間"),
    ("Boardroom Configuration", "董事會佈局"),
    ("Banquet Configuration", "宴會佈局"),
    ("Function Terrace · Yoga Pad · Kids Play · Events Deck", "活動露台 · 瑜伽平台 · 兒童玩水區 · 活動平台"),
    ("Developer Render · Typical Burj Khalifa Stack", "發展商效果圖 · 哈里發塔景觀軸線"),
    ("Living Area with Balcony Access · Burj-Facing", "客廳設露台通道 · 望哈里發塔"),
    ("Dining toward Balcony", "飯廳望向露台"),
    ("Living · Alternate Angle", "客廳 · 另一角度"),
    ("Fitted Kitchen · Premium Appliances", "配備齊全廚房 · 高級電器"),
    ("Balcony · Burj Khalifa View", "露台 · 哈里發塔景觀"),
    ("Main Balcony · Burj Khalifa &amp; Fountain Frontage", "主露台 · 正面望哈里發塔及噴泉"),
    ("Floor-to-ceiling Burj Khalifa frontage", "落地玻璃正面望哈里發塔"),
    ("Private balcony access &nbsp;·&nbsp; Walk-in dressing", "私人露台通道 &nbsp;·&nbsp; 步入式更衣間"),
    ("Private balcony access", "私人露台通道"),
    ("Walk-in dressing area", "步入式更衣間"),
    ("Soaking tub &amp; separate rain shower", "浸浴缸及獨立花灑間"),
    ("Master Bathroom · Vanity", "主人浴室 · 洗手枱"),
    ("Rain Shower &amp; WC", "花灑間及廁所"),
    ("Second Bedroom", "第二睡房"),
    ("Third Bedroom", "第三睡房"),
    ("Maid's Room", "工人房"),
    ("Guest Powder Room", "客用洗手間"),

    # Amenities bullets
    ("<b>Function terrace</b> — double-height atrium for residents' events, with dining tables and landscaped planting.",
     "<b>活動露台</b> — 雙層挑高中庭，可舉辦住戶活動，配有餐桌及景觀植栽。"),
    ("<b>Function terrace</b> — double-height atrium for residents' events.",
     "<b>活動露台</b> — 雙層挑高中庭，可舉辦住戶活動。"),
    ("<b>Yoga pad</b> — open-air deck under mature shade trees, set up for morning practice.",
     "<b>瑜伽平台</b> — 樹蔭遮蔭的露天平台，適合晨間練習。"),
    ("<b>Yoga pad</b> — open-air deck under mature shade trees.",
     "<b>瑜伽平台</b> — 樹蔭遮蔭的露天平台。"),
    ("<b>Children's splash pad</b> — supervised water-play deck with sun-shades, alongside the Qix Club.",
     "<b>兒童玩水區</b> — 有監督的玩水平台，配遮陽棚，毗鄰 Qix 俱樂部。"),
    ("<b>Children's splash pad</b> — supervised water-play deck.",
     "<b>兒童玩水區</b> — 有監督的玩水平台。"),
    ("<b>Events deck</b> — al-fresco dining and entertainment area facing the Marina skyline.",
     "<b>活動平台</b> — 露天用餐及娛樂區，正面望向碼頭天際線。"),
    ("<b>Events deck</b> — al-fresco dining facing the Marina skyline.",
     "<b>活動平台</b> — 露天用餐區，正面望向碼頭天際線。"),
    ("Plus the <b>outdoor pool</b>, <b>24/7 gym</b>, <b>Vida spa</b>, <b>three lounges</b> and the <b>co-working\n        floor</b> covered in the previous spreads.",
     "另設前文介紹的<b>戶外泳池</b>、<b>24 小時健身房</b>、<b>Vida 水療</b>、<b>三個休憩廳</b>及<b>共享工作層</b>。"),

    # Stat strip labels
    ("In-house", "樓內"),
    ("Via Mall", "經商場"),
    ("Hotel keys", "酒店房間"),
    ("To the Mall", "至商場"),
    ("Storeys", "樓層"),

    # Contact card
    ("Your Advisor", "您的物業顧問"),
    ("Real Estate Advisor · Pangea Properties · RERA ORN 23724",
     "物業顧問 · Pangea Properties · RERA ORN 23724"),
    ("Real Estate Advisor · Pangea Properties", "物業顧問 · Pangea Properties"),
    ("Raj Tomar · Real Estate Advisor", "Raj Tomar · 物業顧問"),

    # Three lounge sub-titles
    ("Daylight Lounge", "日光休憩廳"),
    ("Library Lounge", "圖書館休憩廳"),
    ("Atrium Lounge", "中庭休憩廳"),

    # Spec rows (right-side values)
    ("3 + maid's room", "3 + 工人房"),
    ("3 + powder room", "3 + 客用洗手間"),
    ("1,693 sqft / 157 sqm", "1,693 平方呎 / 157 平方米"),
    ("Fully furnished · premium", "全套高級傢俬"),
    ("Fully furnished", "全套傢俬"),
    ("Fully fitted · integrated appliances", "配備齊全 · 嵌入式電器"),
    ("Fully fitted · integrated", "配備齊全 · 嵌入式"),
    ("2 covered bays", "2 個有蓋車位"),
    ("Full Burj + Dubai Fountain", "哈里發塔 + 杜拜噴泉"),
    ("Burj + Dubai Fountain", "哈里發塔 + 杜拜噴泉"),
    ("Burj + Fountain", "哈里發塔 + 噴泉"),
    ("Large panoramic balcony", "大型全景露台"),
    ("Large panoramic", "大型全景"),
    ("22 May 2026", "2026 年 5 月 22 日"),
    ("238 m · 55 storeys", "238 米 · 55 層"),
    ("195-key Vida Dubai Mall", "Vida Dubai Mall · 195 間客房"),
    ("Freehold · Golden Visa eligible", "永久業權 · 可申請黃金簽證"),
    ("Freehold · Golden Visa", "永久業權 · 黃金簽證"),
    ("Branded &amp; serviced · DTCM short-stay", "品牌管理 · DTCM 短租許可"),
    ("Branded &amp; serviced", "品牌管理"),
    ("Private air-conditioned sky-bridge", "私人冷氣天橋"),
    ("Private sky-bridge", "私人天橋"),
    ("Burj Khalifa · DLD zone", "哈里發塔區 · DLD"),
    ("Burj Khalifa · DLD", "哈里發塔 · DLD"),
    ("Complete · handed over · ready", "已落成 · 已交付 · 即住"),
    ("Complete · ready", "已落成 · 即住"),
    ("Ready · Furnished", "即住 · 配備齊全"),
    ("3 BR + Maid", "3 房 + 工人房"),
    ("1,693 sqft", "1,693 平方呎"),
    ("3 venues", "3 個場所"),
    ("All-day", "全日供餐"),
    ("200+ F&amp;B", "200+ 食肆"),

    # === Tower / titles (after the longer phrases above) ===
    ("Vida Dubai Mall · Tower 1 · 3 BR", "Vida Dubai Mall · 一號塔 · 三房"),
    ("Vida Dubai Mall · Tower 1", "Vida Dubai Mall · 一號塔"),
    ('Vida Dubai Mall<br/><b style="font-weight:700;">Tower 1</b>',
     'Vida Dubai Mall<br/><b style="font-weight:700;">一號塔</b>'),

    # === Multi-word labels (BEFORE single-word generics) ===
    ("Three-bedroom serviced residence", "三房服務式住宅"),
    ("Property Brochure", "物業簡介"),
    ("Travel &amp; live", "旅居兩用"),
    ("Parking &amp; access", "車位及通道"),
    ("High floor", "高層單位"),
    ("Mall access", "商場通道"),
    ("The Unit", "單位資料"),
    ("The Building", "大廈資料"),

    # ============================================================
    # === St. Regis specific (must precede generic terms below) ===
    # ============================================================

    # St. Regis full paragraphs (landscape, 10-space indent)
    ("Alongside the Vida Dubai Mall residence, a second option has just come to hand\n          that I'd like to present for your principal's consideration: the\n          <b>St. Regis Residences, Downtown Dubai · Tower 1</b>.",
     "繼 Vida Dubai Mall 單位之後，現再為您客戶呈上另一個值得考慮的選擇 — <b>St. Regis Residences, Downtown Dubai · 一號塔</b>。"),
    ("We have <b>four units available on the 55<sup>th</sup> floor</b> — 5501, 5502,\n          5503 and 5510 — directly from the developer. <b>Handover is scheduled for\n          end of 2026</b>, so this is an off-plan position with payment phased through\n          the build period.",
     "我們可直接由發展商提供<b>位於 55 樓的四個單位</b> — 5501、5502、5503 及 5510。<b>預定 2026 年底交付</b>，屬樓花單位，付款隨工程進度分期支付。"),

    # St. Regis full paragraphs (portrait, 6-space indent)
    ("Alongside the Vida Dubai Mall residence, a second option has just come to hand\n      that I'd like to present for your principal's consideration: the\n      <b>St. Regis Residences, Downtown Dubai · Tower 1</b>.",
     "繼 Vida Dubai Mall 單位之後，現再為您客戶呈上另一個值得考慮的選擇 — <b>St. Regis Residences, Downtown Dubai · 一號塔</b>。"),
    ("We have <b>four units available on the 55<sup>th</sup> floor</b> — 5501, 5502,\n      5503 and 5510 — directly from the developer. <b>Handover is scheduled for\n      end of 2026</b>, so this is an off-plan position with payment phased through\n      the build period.",
     "我們可直接由發展商提供<b>位於 55 樓的四個單位</b> — 5501、5502、5503 及 5510。<b>預定 2026 年底交付</b>，屬樓花單位，付款隨工程進度分期支付。"),
    ("I can arrange a site visit to the St. Regis Residences podium and the show\n      apartment, alongside the Vida Dubai Mall viewing. Floor plans and pricing for\n      units 5501, 5502, 5503 and 5510 will follow under separate cover from the\n      developer.",
     "本人可安排視察 St. Regis Residences 設施平台及示範單位，並可同時前往 Vida Dubai Mall 視察。5501、5502、5503 及 5510 單位之平面圖及價格將由發展商另函提供。"),

    # Standalone labels
    (">Payment</div>", ">付款</div>"),
    (">Status</div>", ">狀態</div>"),
    (">Floor</div>", ">樓層</div>"),
    (">Brand</div>", ">品牌</div>"),
    (">Location</div>", ">位置</div>"),
    (">Units available</div>", ">可選單位</div>"),

    ("The principal differences from the Vida option: a higher floor with broader\n          downtown reach, the <b>St. Regis brand</b> (Marriott) operating the residences,\n          and a fresh-from-developer delivery rather than the ready-furnished Vida unit.",
     "與 Vida 單位之主要分別：本盤位處更高樓層、市中心景觀更廣闊，由 <b>St. Regis（Marriott 旗下）</b>品牌營運，並由發展商全新交付，而非 Vida 已配備齊全的成屋單位。"),
    ("A place unlike any other, Downtown Dubai is where record-breaking is the norm.\n      It is the only place where you can take a walk past the world's tallest tower\n      or enjoy the captivating choreography of the world's largest fountain show.",
     "杜拜市中心是獨一無二的所在，紀錄屢創新高乃是常態。在此可漫步於全球最高塔樓旁，或欣賞世界最大噴泉表演的迷人編排。"),
    ("Sixty-four floors of branded residence — the dark slim tower at centre — set\n      against the Burj Khalifa and the Address Boulevard cluster, with the podium\n      pool deck wrapping the base.",
     "64 層品牌住宅 — 中央的修長深色塔樓 — 與哈里發塔及 Address Boulevard 群樓相映，平台泳池環繞塔基。"),
    ("The St. Regis Residences, Downtown Dubai sit at the foot of the\n          <b>Burj Khalifa</b>, opposite the Dubai Opera and the Dubai Fountain. Tower 1\n          is the original tower of the development.",
     "St. Regis Residences, Downtown Dubai 座落於<b>哈里發塔</b>腳下，正對杜拜歌劇院及杜拜噴泉。一號塔為本發展項目的首座建成塔樓。"),
    ("Designed to the exacting standards of the St. Regis brand, homes range from\n          one to three bedrooms and have been carefully positioned to capture the open\n          views of Burj Khalifa, Dubai Opera and The Dubai Fountain.",
     "依照 St. Regis 品牌嚴謹標準設計，單位由一房至三房不等，並經過悉心定位，盡覽哈里發塔、杜拜歌劇院及杜拜噴泉之開闊景觀。"),
    ("The St. Regis brand sets the standard in premiere personalised living experiences.\n      Downtown Dubai is the hallmark of luxury living celebrating the quintessential,\n      the rare and the exquisite.",
     "St. Regis 品牌乃個人化頂級生活體驗的典範。本項目代表杜拜市中心奢華生活之標誌 — 經典、稀有、精緻。"),
    ("Homes are carefully positioned to capture the open views of <b>Burj Khalifa</b>,\n      Dubai Opera and The Dubai Fountain — the three icons that define this district —\n      with interiors and finishes that harmonise with the tower's architecture and aesthetic.",
     "住宅單位經悉心定位，盡覽<b>哈里發塔</b>、杜拜歌劇院及杜拜噴泉 — 此區三大地標 — 而室內設計與裝修均與塔樓建築美學相互呼應。"),
    ("Interiors are finished to St. Regis specification: stone and warm timber palette,\n      integrated kitchen, full-height glazing onto the balconies and the Downtown skyline.\n      Layouts run from one to three bedrooms; the units offered here are on the 55<sup>th</sup> floor.",
     "室內裝修依 St. Regis 規格完成：石材配暖木調色系、嵌入式廚房、落地玻璃通往露台及市中心天際線。間隔由一房至三房；此處呈獻之單位均位於 55 樓。"),
    ("A resort-scaled pool set across the podium deck, framed by mature palms, sun-shades\n      and private cabanas — open to the residents of all three towers.",
     "度假級泳池橫跨整個平台，配以茂盛棕櫚樹、遮陽設施及私人涼亭 — 供三座塔樓住戶共用。"),
    ("Set across an ultra-modern landscaped podium that connects the three towers,\n          with views over the Dubai Opera promenade.",
     "設置於連接三座塔樓的超現代景觀平台，可俯瞰杜拜歌劇院長廊。"),
    ("Step out and you are on Sheikh Mohammed bin Rashid Boulevard, with the Dubai Opera\n      to the left, Burj Park ahead and The Dubai Mall a four-minute walk away.",
     "踏出大門即抵謝赫穆罕默德本拉希德大道 — 杜拜歌劇院在左、哈里發塔公園在前、杜拜購物中心步行四分鐘可達。"),
    ("I can arrange a site visit to the St. Regis Residences podium and the show\n      apartment, alongside the Vida Dubai Mall viewing. Floor plans and pricing for\n      units 5501, 5502, 5503 and 5510 will follow under separate cover from the\n      developer.",
     "本人可安排視察 St. Regis Residences 設施平台及示範單位，並可同時前往 Vida Dubai Mall 視察。5501、5502、5503 及 5510 單位之平面圖及價格將由發展商另函提供。"),
    ("For the principal who wants <b>brand-new and branded</b>, this is the closer\n      match. For the principal who wants <b>move-in-ready this year</b>, the Vida\n      Dubai Mall unit remains the better fit.",
     "若客戶傾向<b>全新及品牌管理</b>，本盤更為合適；若客戶傾向<b>今年即可入住</b>，Vida Dubai Mall 單位仍為更佳之選。"),
    ("All renders, location indications and amenity descriptions extracted from the\n      Emaar St. Regis Residences developer brochure. The St. Regis Residences,\n      Downtown Dubai are not owned, developed or sold by Marriott International, Inc.\n      Emaar Properties PJSC uses the St. Regis marks under licence from Marriott.\n      Final commercial terms subject to confirmation against the SPA and RERA Form F.",
     "所有效果圖、位置標示及設施描述均取自 Emaar St. Regis Residences 發展商小冊子。St. Regis Residences, Downtown Dubai 並非由 Marriott International, Inc. 擁有、開發或銷售。Emaar Properties PJSC 取得 Marriott 授權使用 St. Regis 品牌。最終商業條款須以 SPA 及 RERA F 表為準。"),

    # Personal note specifics
    ("Personal Note &nbsp;·&nbsp; A Second Option", "個人信函 &nbsp;·&nbsp; 另一選擇"),
    ("St. Regis vs. Vida — at a glance", "St. Regis 與 Vida — 一覽"),

    # Comparison matrix labels & cells
    ("Off-plan · Handover end of 2026", "樓花 · 2026 年底交付"),
    ("55<sup>th</sup> floor — broader downtown views", "55 樓 — 市中心景觀更廣闊"),
    ("5501 · 5502 · 5503 · 5510 — choice of layouts", "5501 · 5502 · 5503 · 5510 — 多款間隔可選"),
    ("St. Regis (Marriott International) — global luxury", "St. Regis（Marriott 旗下）— 國際奢華品牌"),
    ("3 min walk to Burj Khalifa · 4 min to Dubai Mall · 1 min to Dubai Opera",
     "步行 3 分鐘至哈里發塔 · 4 分鐘至杜拜購物中心 · 1 分鐘至杜拜歌劇院"),
    ("Phased through build — direct from Emaar", "隨工程進度分期付款 — 直接由 Emaar 銷售"),

    # Headlines
    ("The hallmark of<br/><b>distinction</b>.", "卓越非凡<br/>的<b>標誌</b>。"),
    ("Tower 1,<br/><b>at street level</b>.", "一號塔，<br/><b>街景一覽</b>。"),
    ("Live in the<br/><b>centre of it all.</b>", "盡享<br/><b>城市中心地段。</b>"),
    ("Simply<br/><b>iconic.</b>", "經典<br/><b>傳奇。</b>"),
    ("Come home to<br/><b>legendary style.</b>", "回家盡享<br/><b>傳奇格調。</b>"),
    ("Unique spaces,<br/><b>unmatched views</b>.", "獨特空間，<br/><b>無與倫比之景觀</b>。"),
    ("The <b>ultimate</b> in<br/>comfort &amp; luxury.", "<b>極致</b>舒適<br/>與奢華。"),
    ("Relax<br/>and <b>unwind</b>.", "放鬆<br/><b>身心</b>。"),
    ("An <b>urban retreat</b><br/>across the podium.", "<b>都市靜謐之地</b><br/>橫跨整個平台。"),
    ("<b>Four units</b><br/>on the 55<sup>th</sup> floor.", "<b>四個單位</b><br/>位於 55 樓。"),
    ("Four units<br/><b>on the 55<sup>th</sup> floor.</b>", "四個單位<br/><b>位於 55 樓。</b>"),
    ("Extraordinary living<br/>in a <b>cosmopolitan city</b>.", "非凡生活<br/><b>於國際都會</b>。"),
    ("Let's discuss<br/>the <b>options.</b>", "讓我們一同<br/>探討<b>選擇。</b>"),

    # Section labels (St. Regis brochure)
    ("01 &nbsp;·&nbsp; The Address", "01 &nbsp;·&nbsp; 地段"),
    ("02 &nbsp;·&nbsp; The Tower", "02 &nbsp;·&nbsp; 塔樓"),
    ("03 &nbsp;·&nbsp; The Building", "03 &nbsp;·&nbsp; 大廈介紹"),
    ("04 &nbsp;·&nbsp; The Brand", "04 &nbsp;·&nbsp; 品牌"),
    ("05 &nbsp;·&nbsp; The View", "05 &nbsp;·&nbsp; 景觀"),
    ("06 &nbsp;·&nbsp; The Interiors", "06 &nbsp;·&nbsp; 室內設計"),
    ("07 &nbsp;·&nbsp; The Pool", "07 &nbsp;·&nbsp; 泳池"),
    ("08 &nbsp;·&nbsp; Amenities", "08 &nbsp;·&nbsp; 會所設施"),
    ("09 &nbsp;·&nbsp; Available Units", "09 &nbsp;·&nbsp; 可選單位"),
    ("10 &nbsp;·&nbsp; Floor Plan", "10 &nbsp;·&nbsp; 平面圖"),
    ("10 &nbsp;·&nbsp; The Neighbourhood", "10 &nbsp;·&nbsp; 周邊環境"),
    ("11 &nbsp;·&nbsp; Specifications", "11 &nbsp;·&nbsp; 規格"),
    ("12 &nbsp;·&nbsp; Next Steps", "12 &nbsp;·&nbsp; 下一步"),

    # Cover - St. Regis brochure
    ("The St. Regis<br/><b>Residences</b><br/>", "St. Regis<br/><b>Residences</b><br/>"),
    ("Downtown Dubai · Tower 1", "Downtown Dubai · 一號塔"),
    ("Four units on the <b>55<sup>th</sup> floor</b>", "四個單位 · 位於 <b>55 樓</b>"),
    ("Off-plan &nbsp;·&nbsp; Handover end of 2026 &nbsp;·&nbsp; Branded by St. Regis",
     "樓花 &nbsp;·&nbsp; 2026 年底交付 &nbsp;·&nbsp; St. Regis 品牌管理"),

    # Captions, walking minutes
    ("min walk to", "分鐘步行至"),
    ("The Dubai Mall", "杜拜購物中心"),
    ("The Dubai Fountain", "杜拜噴泉"),
    ("Dubai Opera", "杜拜歌劇院"),

    # Stat labels & values
    ("Branded by", "品牌管理"),
    ("End 2026", "2026 年底"),
    ("Handover", "交付"),
    ("Tower 1", "一號塔"),

    # Specs table (St. Regis specifics)
    ("The Offer", "本盤資料"),
    ("Units", "單位"),
    ("Configurations", "間隔"),
    ("1–3 bedroom", "1-3 房"),
    ("Branded fit-out · unfurnished", "品牌裝修 · 未配傢俬"),
    ("Burj Khalifa · Opera · Fountain", "哈里發塔 · 歌劇院 · 噴泉"),
    ("Off-plan · Handover end 2026", "樓花 · 2026 年底交付"),
    ("Direct from Emaar", "直接由 Emaar 銷售"),
    ("Phased through build", "隨工程進度分期"),
    ("Brand", "品牌"),
    ("St. Regis (Marriott International)", "St. Regis（Marriott 旗下）"),
    ("Resort podium · F&amp;B service", "度假式平台 · 餐飲服務"),
    ("Spa, sauna, steam, fitness", "水療、桑拿、蒸氣、健身"),
    ("Kids' pool &amp; play area", "兒童泳池及遊樂區"),
    ("Sheikh Mohammed bin Rashid Blvd", "謝赫穆罕默德本拉希德大道"),
    ("Wellness", "健康設施"),
    ("Family", "家庭設施"),
    ("Pool", "泳池"),
    ("Location", "位置"),

    # Floor plan page metadata
    ("1 Bedroom · Type D", "1 房 · D 型"),
    ("2 Bedroom · Type F1", "2 房 · F1 型"),
    ("3 Bedroom · Type D", "3 房 · D 型"),
    ("Suite area", "套房面積"),
    ("Total", "總面積"),
    ("Position", "位置"),
    ("Corner · two balconies", "角位 · 雙露台"),
    ("Two bedrooms · single balcony", "兩房 · 單露台"),
    ("Three bedrooms · wrap balcony", "三房 · 環繞露台"),

    # Unit card chips on Available Units page
    ("Unit · Type 1 BR D", "單位 · 1 房 D 型"),
    ("Unit · Type 2 BR F1", "單位 · 2 房 F1 型"),
    ("Unit · Type 3 BR D", "單位 · 3 房 D 型"),
    ("Suite", "套房"),
    ("Bedrooms", "睡房數"),
    ("1 BR", "1 房"),
    ("2 BR", "2 房"),
    ("3 BR", "3 房"),

    # Photo caption
    ("Developer Render · Tower 1 from Sheikh Mohammed bin Rashid Boulevard",
     "發展商效果圖 · 由謝赫穆罕默德本拉希德大道遠眺一號塔"),
    ("Developer Render · Typical Living Area Towards Burj Khalifa",
     "發展商效果圖 · 典型客廳望哈里發塔"),

    # Amenities bullets (St. Regis)
    ("<b>F&amp;B serviced pool</b> with cabanas", "<b>餐飲服務泳池</b>，設私人涼亭"),
    ("<b>Spa treatment rooms</b> · sauna &amp; steam", "<b>水療療程室</b> · 桑拿及蒸氣浴"),
    ("<b>Fitness centre</b> — 24-hour access", "<b>健身中心</b> — 24 小時開放"),
    ("<b>Community retail</b> on the podium", "<b>社區零售</b>於平台層"),
    ("<b>Barbecue areas</b> across the gardens", "<b>燒烤區</b>遍佈園區"),
    ("<b>Kids' pool</b> &amp; supervised play area", "<b>兒童泳池</b>及有監督遊樂區"),
    ("<b>Resident lounges</b> — daytime &amp; evening", "<b>住戶休憩廳</b> — 日間及晚間"),

    # Brand bullets (St. Regis)
    ("<b>Grand signature staircase</b> — arrival sequence in the manner of the brand.",
     "<b>標誌性華麗樓梯</b> — 品牌專屬的入門儀式。"),
    ("<b>Great Hall</b> — double-height lobby with curated art and a residents' library.",
     "<b>宏偉大廳</b> — 雙層挑高大堂，配以精選藝術品及住戶圖書館。"),
    ("<b>Residential lounges</b> — distinct daytime and evening spaces.",
     "<b>住戶休憩廳</b> — 日間與晚間各有獨特空間。"),
    ("<b>St. Regis butler service</b> — available to residents on request.",
     "<b>St. Regis 管家服務</b> — 住戶可預約使用。"),

    # Spec stat strip on Simply Iconic
    ("Tower", "塔樓"),
    ("Floor", "樓層"),

    # Building intro for St. Regis context (longer copy)
    ("Bedrooms", "睡房數"),
    ("Burj Khalifa", "哈里發塔"),


    # === Single-word generics LAST ===
    ("Configuration", "間隔"),
    ("Furnishing", "傢俬"),
    ("Bathrooms", "浴室"),
    ("Bedrooms", "睡房"),
    ("Kitchen", "廚房"),
    ("Parking", "車位"),
    ("Balcony", "露台"),
    ("Available", "可入住"),
    ("Developer", "發展商"),
    ("Tenure", "業權"),
    ("Status", "狀態"),
    ("Service", "服務"),
    ("Height", "高度"),
    ("Hotel", "酒店"),
    ("Amenities", "會所設施"),
    ("Connectivity", "交通連繫"),
    ("Size", "面積"),
    ("View", "景觀"),
    ("Access", "使用權"),
    ("Zone", "地段"),
    ("Residents", "僅限住戶"),
]


CJK_CSS = """
  /* === Cantonese / Traditional Chinese typography === */
  .display, .display-sm, .h2, .h3, .lead, .body, .section-tag,
  .panel-title, .panel-body, .panel-eyebrow,
  .stat-label, .stat-value, .fact-label, .fact-value,
  .col-title, .arrow-list li, .specs .key, .specs .val,
  .caption, .photo-cap, .contact-card .name, .contact-card .role,
  .topbar-right, .footer, .disclaimer,
  h1, h2, p, div, span, li {
    font-family: 'Manrope', 'Inter', 'Noto Sans TC', sans-serif;
  }
  .display, .display-sm, .h2, .h3, .panel-title, h1, h2 {
    letter-spacing: 0.005em !important;
    text-transform: none !important;
  }
  .section-tag, .panel-eyebrow, .caption, .photo-cap, .col-title,
  .stat-label, .fact-label, .topbar-right, .contact-card .eyebrow,
  .contact-card .role {
    letter-spacing: 0.16em !important;
  }
  .wordmark { letter-spacing: 0.3em !important; }
  .body, .panel-body, .lead, .arrow-list li { line-height: 1.7 !important; }
"""


def translate(content):
    for en, zh in TRANSLATIONS:
        content = content.replace(en, zh)
    content = content.replace("</style>", CJK_CSS + "\n</style>")
    content = content.replace("Pangea Properties</title>", "Pangea Properties · 繁體中文版</title>")
    content = content.replace("(Portrait)</title>", "(Portrait · 繁體中文)</title>")
    return content


for src_name in [
    "brochure.html",
    "brochure-portrait.html",
    "brochure-stregis.html",
    "brochure-stregis-portrait.html",
]:
    src_path = Path(src_name)
    if not src_path.exists():
        continue
    out_name = src_name.replace(".html", "-zh.html")
    Path(out_name).write_text(translate(src_path.read_text()))
    print(f"Created {out_name}")
