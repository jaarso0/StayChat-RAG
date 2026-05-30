

import os
import re
from collections import Counter


def clean_filename(name: str) -> str:
    name = name.replace("&", "And")
    name = re.sub(r"[^\w\-]", "_", name)
    return re.sub(r"_+", "_", name).strip("_")


## HOTEL DESCRIPTIONS


DESCRIPTIONS = [
    {
        "hotel_name": "Burj Al Arab",
        "text": '''<p>BURJ AL ARAB â€” DUBAI, UAE</p>

<p>Rising 321 metres above the Arabian Gulf on its own artificial island,  the Burj Al Arab is widely regarded as one of the worldâ€™s most luxurious hotels.&nbsp;&nbsp;Designed by architect Tom Wright of WS Atkins, the sail-shaped silhouette has become an icon of modern Dubai.</p>

<p>The hotel features 202 duplex suites â€” the smallest spanning 170 sqm and the Royal Suite stretching over 780 sqm.  Every suite offers panoramic views of the Gulf through floor-to-ceiling windows.   The interiorâ€™s design blends Arabian opulence with contemporary luxury: marble floors, gold leaf accents,  and bespoke furnishings.</p>

The atrium lobby soars 180 metres high â€” one of the tallestÂ in the world â€” featuring a dramatic fountain display  and vibrant colour scheme.&nbsp; Guests arrive via a dedicated bridge from the mainland, with Rolls-Royce  transfers available as standard for suite bookings.

<div class='note'>Star Rating: Often described as â€œ7-starâ€\x9d (officially 5-star deluxe)</div>

© 2024 HotelCorp. All rights reserved. | Privacy Policy | Terms'''
    },
    {
        "hotel_name": "The Ritz London",
        "text": '''<div class='hotel-desc'>
the RITZ london â€” piccadilly, LONDON

Opened in 1906 by the legendary hotelier CÃ©sar Ritz, The Ritz London is a Grade II listed building on Piccadilly&nbsp;overlooking Green Park.  The hotel is synonymous with  British elegance and has hosted royalty, heads of state, and celebrities for over a century.

<p>The 136 rooms and suites are decorated in Louis XVI style with gilded furnishings, ornate plasterwork,  and hand-painted ceilings.&nbsp;&nbsp; Each room features marble bathrooms, bespoke toiletries, and views of Piccadilly or  Green Park.</p>

The Palm Court is world-famous  for its afternoon tea â€” a tradition dating back to the hotelâ€™s opening. The Ritz Restaurant serves classic French cuisine  beneath a stunning ceiling painted to resemble a summer sky.
</div>
<div class='footer'>© 2024 Luxury Hotels International. All rights reserved. | Privacy Policy | Terms of Service | Cookie Settings</div>'''
    },
    {
        "hotel_name": "Marina Bay Sands",
        "text": '''marina bay sands â€” SINGAPORE

<p>Marina Bay Sands is an integrated resort  fronting Marina Bay in Singapore.&nbsp;  Developed by Las Vegas Sands Corp at a cost of US$8&nbsp;billion, it opened in 2010 and has become Singaporeâ€™s most recognisable landmark.</p>

The resort comprises three 55-storey towers  connected at the top by the 340-metre SkyPark â€” home to the worldâ€™s most famous infinity pool.&nbsp;&nbsp;  The complex includes a 2,561-room hotel, a convention-exhibition centre,  the Shoppes mall (800+ retailers), a museum, two theatres,  and a casino.

<p>Rooms feature floor-to-ceiling windows  with either city or bay views.  Premier Rooms start at 39 sqm, while the Chairman Suite spans  600 sqm across the top floor of Tower 1.</p>

This page was last updated on 2024-03-15.&nbsp;&nbsp;© HotelReviews.com&nbsp;|&nbsp;About Us&nbsp;|&nbsp;Contact'''
    },
    {
        "hotel_name": "Waldorf Astoria New York",
        "text": '''<div><h2>WALDORF ASTORIA NEW YORK</h2></div>

<p>The Waldorf Astoria  New York is a landmark Art Deco hotel on Park Avenue in midtown Manhattan.&nbsp; Originally opened in 1931, it was for decades the worldâ€™s largest  and tallest hotel.  The building is a designated New York City landmark.</p>

The hotel features  1,413 rooms including the famous Presidential Suite (used by every sitting US President   since Herbert Hoover) and the Waldorf Towers â€” a luxury hotel-within-a-hotel  occupying floors 27â€”42.

<p>The lobby is celebrated for its Art Deco   grandeur: the â€œWheel of Lifeâ€\x9d mosaic floor, the iconic four-sided bronze clock,  and silver-and-gold coffered ceilings.&nbsp;  The Starlight Roof ballroom  hosted legendary performances from Cole Porter to Frank Sinatra.</p>

<p class='disclaimer'>The information on this page is provided â€œas isâ€\x9d without warranty. Prices and availability subject to change.</p>
© 2024 TravelInfo Ltd. | GDPR | Sitemap'''
    },
    {
        "hotel_name": "The Peninsula Hong Kong",
        "text": '''THE PENINSULA HONG KONG

<p>Known as the â€˜Grande Dame of the Far East,â€™  The Peninsula Hong Kong has been the cityâ€™s  most prestigious hotel since opening in 1928.&nbsp; Located on Salisbury Road in Tsim Sha Tsui,  it overlooks Victoria Harbour and the Hong Kong Island skyline.</p>

the hotel underwent a major expansion  in 1994, adding a 30-storey tower to the original colonial building.   Today it offers 300 rooms and suites â€” all  featuring the hotelâ€™s signature in-room technology  including a custom tablet that controls lighting,&nbsp; curtains, temperature, and entertainment.

<p>The Peninsula is famous for  its fleet of 14 Rolls-Royce Extended Wheelbase Phantoms â€”  the largest such fleet of any hotel in the world.  An Airbus H135 helicopter  offers transfers to Macau and scenic tours of the harbour.</p>

---\nPowered by HotelStack CMS v3.2.1 | Page generated in 0.034s\n<script>var analytics='UA-000000-1';</script>'''
    },
    {
        "hotel_name": "Hotel del Coronado",
        "text": '''<span class='title'>hotel DEL CORONADO â€” coronado, CALIFORNIA</span>

The Hotel del Coronado (locally known as â€˜The Delâ€™)  is a historic beachfront resort in Coronado, California,&nbsp; just across the bay from San Diego.  Built in 1888, it is one of the few surviving examples of an American  Victorian beach resort.

<p>The original Victorian Building features  the iconic red-roofed, white wooden architecture  that has appeared in dozens of films, most famously â€œSome Like It Hotâ€\x9d  (1959) starring Marilyn Monroe.  The Crown Room â€” with its stunning sugar-pine ceiling  constructed without a single nail â€” remains  one of the hotelâ€™s architectural highlights.</p>

In 2001 the property was expanded  with the addition of The Shore, a contemporary oceanfront tower.&nbsp;&nbsp; Today the resort offers 757 rooms  and suites across three distinct accommodation styles.</

<footer>
<nav>Home | About | Hotels | Reviews | Contact Us</nav>
<p>© 2023-2024 StayGuide Inc. All rights reserved.</p>
</footer>'''
    },
    {
        "hotel_name": "Atlantis Paradise Island",
        "text": '''ATLANTIS PARADISE ISLAND,  nassau, bahamas

<p>Atlantis Paradise Island  is a mega-resort on Paradise Island in the Bahamas.&nbsp; The resort is themed around the myth of the lost city  of Atlantis  and is operated by Brookfield Asset Management.</p>

The property is dominated by  the Royal Towers â€” twin 23-storey towers connected by a bridge suite  (â€œThe Bridgeâ€\x9d) that spans the gap 23 storeys above  the lagoon below.&nbsp;  The resort also includes The Coral,  The Beach, The Reef (a luxury all-suite tower),  and The Cove â€” an adults-preferred  boutique hotel.

<p>The centrepiece is Aquaventure,  a 141-acre waterpark featuring over 20 water slides,  a mile-long river ride, and 20 swimming areas.  The Leap of Faith â€” a near-vertical  60-foot drop through a clear acrylic tunnel  submerged in a shark-filled lagoon â€” is the parkâ€™s signature attraction.</p>

<!-- Google Tag Manager -->
© 2024 Premium Hotels Group  |  Do Not Sell My Info  |  Accessibility  |  Sitemap'''
    },
    {
        "hotel_name": "One&Only Royal Mirage",
        "text": '''<div class='hotel-page'>
one&amp;only ROYAL MIRAGE â€” dubai, UAE

Set within 65 acres  of landscaped gardens along Jumeirah Beach, One&amp;Only Royal Mirage  is a low-rise, Moorish-inspired luxury resort.&nbsp;&nbsp;  Unlike Dubaiâ€™s glass-and-steel towers, this property offers  an intimate, old-world Arabian atmosphere.

<p>The resort comprises three distinct  properties: The Palace (the original and grandest), Arabian Court  (with its Moorish courtyards and fountains),  and Residence &amp; Spa (an exclusive enclave of 49 prestige rooms).&nbsp; Together they offer 453 rooms and suites.</p>

the kilometre-long private beach  is one of the most uncrowded in Dubai.  Lush gardens feature  meandering pathways, traditional Arabic lanterns,  and reflecting pools that create a serene atmosphere  unlike any other Dubai resort.
</div>

© 2024 HotelCorp. All rights reserved. | Privacy Policy | Terms'''
    },
]

##HOTEL REVIEWS

REVIEWS = [
    {
        "hotel_name": "Burj Al Arab",
        "text": '''<div class='review-card'>
<span class='stars'>â˜…â˜…â˜…â˜…â˜…</span>
guest REVIEW â€” Burj Al Arab

Absolutely breathtaking experience.  The moment we stepped into the atrium lobby, we were overwhelmed by the sheer opulence.&nbsp; Our duplex suite on the 18th floor  offered panoramic views of the Arabian Gulf.  The complimentary Rolls-Royce airport transfer set the tone for our stay.

Breakfast at Sahn Eddar was exquisite â€” fresh pastries, Arabic mezze, and premium coffee.&nbsp;&nbsp;  The private beach was immaculate.  The Al Mahara underwater restaurant was the highlight â€”  dining surrounded by a floor-to-ceiling aquarium.

<p>WiFi was fast and complimentary throughout.  The spa offered a traditional hammam treatment  that was deeply relaxing.  Only downside: the gold-plated iPads  in the room were a bit dated.  Overall, worth every dirham.   Would return in a heartbeat.</p>
</div>

© 2024 HotelCorp. All rights reserved. | Privacy Policy | Terms'''
    },
    {
        "hotel_name": "The Ritz London",
        "text": '''Guest Review â€” THE RITZ LONDON   â˜…â˜…â˜…â˜…â˜…

Quintessential British luxury.&nbsp;  We booked the Deluxe King room  and were upgraded to a Junior Suite  overlooking Green Park.  Afternoon tea in the Palm Court  was magical â€” finger sandwiches,  warm scones with clotted cream,  and a harpist playing in the background.

<p>The Rivoli Bar serves exceptional cocktails.  Staff were attentive without being intrusive.&nbsp;  Free WiFi was available but a bit slow  during peak hours.</p>

Breakfast included a full English  with smoked salmon and scrambled eggs.&nbsp;&nbsp;  Location on Piccadilly is unbeatable â€”  walking distance to Buckingham Palace  and the Royal Academy.  The dÃ©cor is Louis XVI style,  gilded and elegant throughout.

This page was last updated on 2024-03-15.&nbsp;&nbsp;© HotelReviews.com&nbsp;|&nbsp;About Us&nbsp;|&nbsp;Contact'''
    },
    {
        "hotel_name": "Marina Bay Sands",
        "text": '''<div class='user-review'>
Guest review â€” marina bay sands  â˜…â˜…â˜…â˜…â˜†

The infinity pool on the 57th floor  is as stunning as it looks in photos â€”  possibly the most iconic hotel amenity  in the world.  Our Premier Room had excellent views  of the Singapore skyline.

The casino is enormous.&nbsp;  Shopping mall attached is high-end  (Louis Vuitton, Chanel).  WiFi was complimentary and reliable.  Breakfast at RISE restaurant was a vast  international buffet â€” live cooking stations  for eggs, noodles, and dim sum.

<p>However, the hotel feels very large  and impersonal â€”  long walks to elevators, busy lobbies.&nbsp;&nbsp;  Check-in took 25 minutes.  The ArtScience Museum next door  was a wonderful bonus.  Room service was pricey but prompt.  Good value for a bucket-list experience.</p>
</div>
<div class='footer'>© 2024 Luxury Hotels International. All rights reserved. | Privacy Policy | Terms of Service | Cookie Settings</div>'''
    },
    {
        "hotel_name": "Waldorf Astoria New York",
        "text": '''GUEST REVIEW â€” waldorf astoria new york  â˜…â˜…â˜…â˜…â˜†

<p>A piece of New York history.  The Art Deco lobby is magnificent â€” the famous â€œWheel of Lifeâ€\x9d mosaic floor,  the grand clock, and the silver-and-gold ceiling.&nbsp;  Our room was recently renovated and felt fresh:  marble bathroom, Salvatore Ferragamo toiletries,  blackout curtains.</p>

Complimentary WiFi worked well.  Breakfast at Peacock Alley was classic American:  pancakes, eggs Benedict, fresh-pressed juice. &nbsp;&nbsp; Location on Park Avenue  is ideal for midtown attractions.

Staff were professional  but the hotel was undergoing partial renovation during our stay â€”  some noise during mornings.  The Bull &amp; Bear bar downstairs  has legendary Old Fashioneds.  Would recommend requesting  a high-floor room for quieter nights.

<p class='disclaimer'>The information on this page is provided â€œas isâ€\x9d without warranty. Prices and availability subject to change.</p>
© 2024 TravelInfo Ltd. | GDPR | Sitemap'''
    },
    {
        "hotel_name": "The Peninsula Hong Kong",
        "text": '''<div class='review'>
Guest Review â€” the peninsula hong kong  â˜…â˜…â˜…â˜…â˜…

The â€˜Grande Dame of the Far Eastâ€™  lives up to every expectation. &nbsp; Our Deluxe Harbour View room was stunning â€”  floor-to-ceiling windows overlooking Victoria Harbour,  in-room tablet controlling everything from curtains to lighting.

<p>The Rolls-Royce fleet for transfers  is a wonderful touch.  Breakfast at The Lobby had  a continental spread and excellent dim sum.&nbsp;&nbsp;  Free WiFi throughout.  The spa uses ESPA products  and the Roman-style pool is gorgeous.</p>

Felix restaurant on the top floor  (designed by Philippe Starck) has incredible views  and modern European cuisine.  Gaddiâ€™s for fine French dining  was also superb.  Concierge arranged  a harbour cruise on short notice.  Truly world-class service.
</div>

---\nPowered by HotelStack CMS v3.2.1 | Page generated in 0.034s\n<script>var analytics='UA-000000-1';</script>'''
    },
    {
        "hotel_name": "Hotel del Coronado",
        "text": '''guest review â€” HOTEL DEL CORONADO   â˜…â˜…â˜…â˜…â˜†

A stunning Victorian beachfront property.  We stayed in the original Victorian Building  and the room had genuine character â€”  high ceilings, original woodwork,  ocean sounds at night.&nbsp;  The beach is wide, clean,  and right outside the door.

<p>Complimentary WiFi was adequate.&nbsp;&nbsp;  Breakfast at Sheerwater was lovely  with ocean views â€” fresh fruit,  avocado toast, and excellent coffee.  The hotelâ€™s history is fascinating  â€” they say Marilyn Monroe  filmed â€˜Some Like It Hotâ€™ here.</p>

The pool area was well-maintained.  Only negatives: parking is expensive ($45/night),  and some corridors in the old building  feel dated.  The Sunday brunch at Crown Room  is a must.  Great for a romantic getaway  or family beach holiday.

<footer>
<nav>Home | About | Hotels | Reviews | Contact Us</nav>
<p>© 2023-2024 StayGuide Inc. All rights reserved.</p>
</footer>'''
    },
    {
        "hotel_name": "Atlantis Paradise Island",
        "text": '''<div class='review-content'>
GUEST Review â€” atlantis paradise island  â˜…â˜…â˜…â˜†â˜†

Incredible waterpark, average hotel.&nbsp;  The Aquaventure waterpark is world-class â€”  the Leap of Faith slide through the shark tank  was thrilling.  Marine habitat with 50,000 sea creatures  is educational and beautiful.

<p>Our Royal Towers room was spacious  but felt somewhat dated â€”  furniture was worn, bathroom needed updating.&nbsp;&nbsp;  WiFi was complimentary but slow.  Breakfast at Poseidonâ€™s Table  was a buffet with standard resort fare â€”  nothing special but adequate.</p>

The casino is large and lively.  Nobu restaurant on-site was excellent.&nbsp;  Beach was beautiful but can get crowded.  The resort is massive â€”  expect lots of walking.  Good for families with children;  couples seeking a quiet retreat  should look elsewhere.  Room prices feel high  for the room quality,  but youâ€™re paying for the waterpark access.
</div>

<!-- Google Tag Manager -->
© 2024 Premium Hotels Group  |  Do Not Sell My Info  |  Accessibility  |  Sitemap'''
    },
    {
        "hotel_name": "One&Only Royal Mirage",
        "text": '''Guest Review â€” ONE&amp;ONLY ROYAL MIRAGE  â˜…â˜…â˜…â˜…â˜…

<p>The most serene resort in Dubai.  Unlike the flashy towers along Sheikh Zayed Road,  this is a low-rise, Moorish-style property  set in 65 acres of landscaped gardens.&nbsp;  Our Arabian Court room was elegant â€”  dark wood, arabesque patterns,  a private balcony overlooking the palm-lined pools.</p>

The one-kilometre private beach  was uncrowded and pristine.&nbsp;&nbsp;  Breakfast at Olives was Mediterranean  and fresh â€” particularly good shakshuka and labneh.  Complimentary WiFi was excellent.

<p>The Oriental Hammam &amp; Spa  was the best spa experience weâ€™ve ever had.  Celebrities restaurant (fine dining)  served outstanding French-Moroccan cuisine.  Only downside: itâ€™s a 15-minute taxi  to Dubai Mall.  But that isolation is also its charm.&nbsp; Highly recommended for couples.</p>

© 2024 HotelCorp. All rights reserved. | Privacy Policy | Terms'''
    },
    {
        "hotel_name": "Marina Bay Sands",
        "text": '''guest review â€” MARINA BAY SANDS (second visit)  â˜…â˜…â˜…â˜†â˜†

Second visit, and this time was less impressive.&nbsp;  The room in Tower 3 had a city view  which wasnâ€™t as spectacular  as the bay-facing rooms.  Found a stain on the sofa cushion.

<p>The infinity pool was overcrowded on Saturday â€”  had to queue for 15 minutes.&nbsp;&nbsp;  Breakfast buffet at RISE was decent  but chaotic â€” tables not cleared  quickly enough.  WiFi was free and fast though.</p>

The Shoppes at Marina Bay Sands  are great for luxury shopping.  CÃ‰ LA VI rooftop bar  has great cocktails but is pricey.&nbsp;  For this price point,  I expected better room maintenance.  Would try a different Singapore hotel  next time â€” perhaps the Raffles or Fullerton.

This page was last updated on 2024-03-15.&nbsp;&nbsp;© HotelReviews.com&nbsp;|&nbsp;About Us&nbsp;|&nbsp;Contact'''
    },
    {
        "hotel_name": "Burj Al Arab",
        "text": '''<div class='review'>
Guest REVIEW â€” burj al arab (anniversary trip)  â˜…â˜…â˜…â˜…â˜†

Visited for an anniversary trip.  The suite was extraordinary â€” two floors, rotating bed,  jacuzzi with Arabian Gulf views.&nbsp; However, some of the technology  (in-room controls) felt glitchy.

The butler service was exceptional â€”  our butler Rashid anticipated every need.&nbsp;&nbsp;  Dinner at Al Muntaha (27th floor)  was spectacular both in food and views.  Breakfast was complimentary and world-class.

<p>The private beach facilities  were top-notch.  Free WiFi and fast connectivity.  The only letdown:  the Skyview Bar felt like it was catering  more to tourists than hotel guests â€”  long wait even with a reservation.&nbsp;  Still, itâ€™s a once-in-a-lifetime hotel.  The helicopter transfer option  from the rooftop helipad is worth considering  for a special occasion.</p>
</div>
<div class='footer'>© 2024 Luxury Hotels International. All rights reserved. | Privacy Policy | Terms of Service | Cookie Settings</div>'''
    },
]

##HOTEL POLICIES

POLICIES = [
    {
        "hotel_name": "Burj Al Arab",
        "text": '''<div class='policy-page'>
<h3>CANCELLATION &amp; BOOKING POLICY â€” Burj Al Arab</h3>

<p>â€¢ Free cancellation up to 72 hours before check-in date.</p>
<p>â€¢ Cancellations within 72 hours  incur a charge equal to 1 nightâ€™s rate.</p>
â€¢ No-show: full stay charged.
â€¢ Check-in: 3:00 PM&nbsp;|&nbsp;Check-out: 12:00 PM (noon).
â€¢ Early check-in subject to availability  (complimentary for suite guests).
â€¢ Late check-out until 4:00 PM  available at 50% of nightly rate.
<p>â€¢ Pets are NOT permitted on the property.</p>
â€¢ Children of all ages are welcome;  cribs provided free of charge.&nbsp;&nbsp;
â€¢ Valid passport or Emirates ID  required at check-in.
â€¢ Refunds processed within  10â€”14 business days to original payment method.
</div>

© 2024 HotelCorp. All rights reserved. | Privacy Policy | Terms'''
    },
    {
        "hotel_name": "The Ritz London",
        "text": '''cancellation &amp; booking POLICY â€” the Ritz London

â€¢ Free cancellation up to 48 hours  prior to arrival.
â€¢ Cancellations within 48 hours:  1 night charged as penalty.&nbsp;
<p>â€¢ Non-refundable rates available  at 15% discount â€” no cancellation or changes.</p>
â€¢ Check-in: 2:00 PM | Check-out: 11:00 AM.
â€¢ Late check-out until 1:00 PM upon request  (subject to availability).&nbsp;&nbsp;
â€¢ DRESS CODE applies in The Ritz Restaurant  and Palm Court: smart casual minimum,  gentlemen require jacket.
<p>â€¢ Small dogs permitted (under 10 kg)  with prior arrangement â€” Â£50/night surcharge.</p>
â€¢ Children welcome;  interconnecting rooms available on request.
â€¢ Afternoon tea reservations  must be cancelled 24 hours in advance.
â€¢ Refunds issued within 7 business days.

<div class='footer'>© 2024 Luxury Hotels International. All rights reserved. | Privacy Policy | Terms of Service | Cookie Settings</div>'''
    },
    {
        "hotel_name": "Marina Bay Sands",
        "text": '''<div class='policy-section'>
CANCELLATION &amp; BOOKING POLICY  â€” marina bay sands

â€¢ Free cancellation up to 24 hours  before check-in.
â€¢ Cancellations within 24 hours:  first night charged.&nbsp;
â€¢ Advance Purchase rate:  non-refundable, 20% discount.

<p>â€¢ Check-in: 3:00 PM&nbsp;|&nbsp;Check-out: 11:00 AM.</p>
â€¢ Infinity pool access  for hotel guests only  (wristband required).&nbsp;&nbsp;
â€¢ Pets are NOT permitted.
â€¢ CASINO: minimum age 21;  valid ID required for entry.
â€¢ Children under 12 stay free  when sharing parentsâ€™ room.
â€¢ Deposit: 1 nightâ€™s rate + SGD 200 incidentals  charged at booking.
â€¢ Refunds processed within  14 business days.
</div>

This page was last updated on 2024-03-15.&nbsp;&nbsp;© HotelReviews.com&nbsp;|&nbsp;About Us&nbsp;|&nbsp;Contact'''
    },
    {
        "hotel_name": "Waldorf Astoria New York",
        "text": '''Cancellation &amp; Booking Policy â€”  WALDORF ASTORIA new york

<p>â€¢ Free cancellation up to 48 hours  before arrival.</p>
â€¢ Late cancellation or no-show:  1 night charged.
â€¢ Check-in: 4:00 PM | Check-out: 12:00 PM (noon).&nbsp;
â€¢ Early check-in from 1:00 PM  subject to availability  (Hilton Honors Diamond members guaranteed).

â€¢ Pets: dogs under 75 lbs welcome,  $50 non-refundable cleaning fee per stay.&nbsp;&nbsp;
<p>â€¢ Valet parking: $75/night.</p>
â€¢ DESTINATION FEE: $50/night  covers WiFi, fitness center, and local calls.
â€¢ Children under 18 stay free  with an adult.
â€¢ Group bookings (10+ rooms):  separate cancellation terms apply.
â€¢ Refunds within 5â€”10 business days.

<p class='disclaimer'>The information on this page is provided â€œas isâ€\x9d without warranty. Prices and availability subject to change.</p>
© 2024 TravelInfo Ltd. | GDPR | Sitemap'''
    },
    {
        "hotel_name": "The Peninsula Hong Kong",
        "text": '''<div class='policies'>
Cancellation &amp; Booking Policy  â€” THE PENINSULA hong kong

â€¢ Free cancellation up to 48 hours  prior to arrival.&nbsp;
â€¢ Within 48 hours:  full cancellation fee (1 night).
â€¢ Flexible Rate includes  complimentary breakfast for 2.

<p>â€¢ Check-in: 2:00 PM&nbsp;|&nbsp;Check-out: 12:00 PM.</p>
â€¢ Late check-out until 6:00 PM  subject to availability at 50% nightly rate.&nbsp;&nbsp;
â€¢ Pets are NOT permitted.
â€¢ Rolls-Royce airport transfer:  complimentary for suite bookings.
â€¢ Children welcome;  babysitting services available on request.
â€¢ Deposit: 1 night charged  at booking confirmation.
â€¢ Refunds processed  within 7â€”10 business days.
</div>

---\nPowered by HotelStack CMS v3.2.1 | Page generated in 0.034s\n<script>var analytics='UA-000000-1';</script>'''
    },
    {
        "hotel_name": "Hotel del Coronado",
        "text": '''CANCELLATION &amp; booking policy â€”  Hotel del Coronado

â€¢ Free cancellation up to 72 hours  before check-in.
â€¢ Cancellations within 72 hours:  1 night penalty.&nbsp;
<p>â€¢ RESORT FEE: $45/night  (covers WiFi, beach chairs, fitness center, bike rentals).</p>
â€¢ Check-in: 4:00 PM | Check-out: 11:00 AM.

â€¢ Pets: dogs under 40 lbs welcome  in select pet-friendly rooms â€” $150/stay fee.&nbsp;&nbsp;
â€¢ Valet parking: $60/night;  self-parking: $45/night.
â€¢ Children under 17 stay free  with parent.
â€¢ Beach equipment (umbrellas, chairs)  provided complimentary to hotel guests.
â€¢ Holiday and peak season bookings  require 7-day cancellation notice.
â€¢ Refunds within 10 business days.

<footer>
<nav>Home | About | Hotels | Reviews | Contact Us</nav>
<p>© 2023-2024 StayGuide Inc. All rights reserved.</p>
</footer>'''
    },
    {
        "hotel_name": "Atlantis Paradise Island",
        "text": '''<div class='policy-page'>
cancellation &amp; BOOKING POLICY  â€” Atlantis Paradise Island

â€¢ Free cancellation up to 7 days  before arrival.&nbsp;
â€¢ Cancellations within 7 days:  2 nights charged.
<p>â€¢ All-Inclusive Package: non-refundable,  includes meals + Aquaventure access.</p>
â€¢ Check-in: 4:00 PM | Check-out: 11:00 AM.

â€¢ Aquaventure waterpark access:  complimentary for ALL hotel guests  (unlimited during stay).&nbsp;&nbsp;
â€¢ Pets are NOT permitted  on the resort.
â€¢ Children under 12 stay and eat free  (when sharing parentsâ€™ room and dining  at select restaurants).
â€¢ RESORT LEVY: $49.99/night per room.
â€¢ Deposit: 50% of total stay  charged at booking.
â€¢ Refunds processed  within 14â€”21 business days.
</div>

<!-- Google Tag Manager -->
© 2024 Premium Hotels Group  |  Do Not Sell My Info  |  Accessibility  |  Sitemap'''
    },
]

##HOTEL AMENITIES

AMENITIES = [
    {
        "hotel_name": "Burj Al Arab",
        "text": '''<div class='amenities-list'>
<h3>AMENITIES &amp; FACILITIES â€” Burj Al Arab</h3>

<p>â€¢ Complimentary high-speed WiFi  throughout all suites and public areas.</p>
â€¢ Complimentary full breakfast  at Sahn Eddar (atrium restaurant)  for all guests.&nbsp;
â€¢ Private beach with dedicated sun loungers,  parasols, and towel service.
â€¢ Talise Spa: indoor pool,  plunge pools, sauna, steam room,  and treatment suites.&nbsp;&nbsp;
<p>â€¢ Fitness centre: Technogym equipment,  personal training available.</p>
â€¢ 9 restaurants and bars  including Al Mahara (underwater),  Al Muntaha (27th floor),  and Scape (poolside).
â€¢ Dedicated butler service  for every suite (24/7).
â€¢ Chauffeur-driven Rolls-Royce transfer  (complimentary for suite guests).
â€¢ Helipad on the roof â€”  helicopter transfers available.
â€¢ Kidsâ€™ club: Wild Wadi Waterpark access  (complimentary shuttle).
â€¢ Business centre  with meeting rooms and audiovisual equipment.
</div>

© 2024 HotelCorp. All rights reserved. | Privacy Policy | Terms'''
    },
    {
        "hotel_name": "The Ritz London",
        "text": '''amenities &amp; FACILITIES â€” the ritz london

â€¢ Complimentary WiFi  in all rooms and public spaces.&nbsp;
â€¢ Full English breakfast  served at The Ritz Restaurant  (included in most rates).
<p>â€¢ Afternoon Tea at The Palm Court  â€” advance booking essential.</p>
â€¢ The Rivoli Bar: cocktails  in an Art Deco setting.&nbsp;&nbsp;
â€¢ The Ritz Salon:  hair and beauty treatments.
â€¢ Fitness suite with cardiovascular  and weight equipment.
â€¢ Concierge and porter service.
â€¢ In-room dining available 24/7.&nbsp;
â€¢ Florist, shoe shine,  and laundry/dry-cleaning services.
â€¢ William Kent Room:  private dining and event space  (up to 36 guests).
<p>â€¢ NOTE: The Ritz London  does NOT have a swimming pool or spa.</p>

<div class='footer'>© 2024 Luxury Hotels International. All rights reserved. | Privacy Policy | Terms of Service | Cookie Settings</div>'''
    },
    {
        "hotel_name": "Marina Bay Sands",
        "text": '''<div class='hotel-amenities'>
Amenities &amp; Facilities  â€” MARINA BAY SANDS

â€¢ Complimentary WiFi  for all hotel guests.&nbsp;
â€¢ Breakfast buffet at RISE restaurant  (international cuisine, live cooking stations).
<p>â€¢ INFINITY POOL (57th floor, SkyPark):  150-metre pool overlooking the city â€”  hotel guests only.</p>
â€¢ Banyan Tree Spa:  over 50 treatment rooms  on the 55th floor.&nbsp;&nbsp;
â€¢ Fitness centre:  state-of-the-art equipment, open 24/7.
â€¢ Casino: 15,000 sq m gaming floor,  600+ table games, 1,500 slot machines.
â€¢ The Shoppes at Marina Bay Sands:  800+ stores and restaurants.
â€¢ ArtScience Museum:  rotating exhibitions.&nbsp;
â€¢ Sands Theatre:  Broadway shows and concerts.
â€¢ Convention centre:  120,000 sq m of event space.
â€¢ Digital Light Canvas:  interactive art installation.
</div>

This page was last updated on 2024-03-15.&nbsp;&nbsp;© HotelReviews.com&nbsp;|&nbsp;About Us&nbsp;|&nbsp;Contact'''
    },
    {
        "hotel_name": "Waldorf Astoria New York",
        "text": '''AMENITIES &amp; facilities  â€” waldorf astoria new york

â€¢ WiFi included in destination fee  ($50/night).&nbsp;
â€¢ Breakfast at Peacock Alley:  American classics and pastries.
<p>â€¢ The Bull &amp; Bear:  legendary steakhouse and cocktail bar.</p>
â€¢ Guerlain Spa: signature treatments,  couples suites, relaxation lounge.&nbsp;&nbsp;
â€¢ Fitness centre: 24/7 access,  complimentary for guests.
â€¢ Grand Ballroom: 4,400 sq ft,  hosts up to 1,500 guests  (Starlight Roof).
â€¢ Art Deco architectural tours  available (self-guided or concierge-led).
â€¢ Concierge, valet parking,  and car service.&nbsp;
â€¢ Business centre: printing, fax,  meeting pods.
â€¢ Presidential and Royal suites  with private dining rooms.
â€¢ Waldorf Astoria Clock:  iconic four-sided bronze clock  in lobby.

<p class='disclaimer'>The information on this page is provided â€œas isâ€\x9d without warranty. Prices and availability subject to change.</p>
© 2024 TravelInfo Ltd. | GDPR | Sitemap'''
    },
    {
        "hotel_name": "The Peninsula Hong Kong",
        "text": '''<div>
amenities &amp; facilities  â€” THE PENINSULA Hong Kong

â€¢ Complimentary high-speed WiFi  throughout the hotel.&nbsp;
â€¢ Breakfast buffet at The Lobby  (continental + dim sum).
â€¢ The Peninsula Spa by ESPA:  indoor heated pool, jacuzzi, steam rooms.&nbsp;&nbsp;
<p>â€¢ Fitness centre  with harbour views.</p>
â€¢ Fleet of 14 Rolls-Royce  Extended Wheelbase Phantoms.
â€¢ Helicopter service:  Airbus H135 flights to Macau  and scenic tours.
â€¢ Gaddiâ€™s: fine French dining  (Michelin-recommended).&nbsp;
â€¢ Felix: modern European  by Philippe Starck  (panoramic views).
â€¢ The Lobby: famous afternoon tea.
â€¢ Shopping arcade:  premium boutiques at lobby level.
â€¢ In-room technology:  tablet-controlled lighting,  curtains, and TV.
</div>

---\nPowered by HotelStack CMS v3.2.1 | Page generated in 0.034s\n<script>var analytics='UA-000000-1';</script>'''
    },
    {
        "hotel_name": "Hotel del Coronado",
        "text": '''Amenities &amp; Facilities  â€” hotel DEL CORONADO

â€¢ WiFi included in resort fee  ($45/night).&nbsp;
â€¢ Breakfast at Sheerwater:  ocean-view dining, fresh California cuisine.
<p>â€¢ BEACH: 1.5 miles of white sand,  complimentary chairs, umbrellas, and towels.</p>
â€¢ Pool: heated outdoor pool  in the Victorian building courtyard.&nbsp;&nbsp;
â€¢ Spa at The Del:  full-service spa with  ocean-inspired treatments.
â€¢ Fitness centre:  modern equipment, yoga  and Pilates classes.
â€¢ Bike rentals: complimentary  cruiser bikes for guests.&nbsp;
â€¢ Fire pits on the beach  (nightly, complimentary sâ€™mores kits).
â€¢ Babcock &amp; Story Bar:  craft cocktails and live music.
â€¢ Crown Room: Sunday brunch  (reservations recommended).
â€¢ Water sports: surfing lessons,  paddleboarding, kayaking nearby.

<footer>
<nav>Home | About | Hotels | Reviews | Contact Us</nav>
<p>© 2023-2024 StayGuide Inc. All rights reserved.</p>
</footer>'''
    },
    {
        "hotel_name": "Atlantis Paradise Island",
        "text": '''<div class='amenity-details'>
AMENITIES &amp; facilities  â€” atlantis PARADISE island

â€¢ Complimentary WiFi in all rooms  (premium high-speed upgrade available).&nbsp;
â€¢ Breakfast buffet  at Poseidonâ€™s Table.
<p>â€¢ AQUAVENTURE WATERPARK:  141-acre water theme park, 20+ slides  including the Leap of Faith  (60-foot near-vertical drop  through a clear tunnel  in a shark lagoon).</p>
â€¢ Marine Habitat: open-air aquarium  with 50,000+ marine animals.&nbsp;&nbsp;
â€¢ Dolphin Cay:  swim-with-dolphin experiences.
â€¢ Casino: 85,000 sq ft gaming floor.
â€¢ 21 restaurants and bars  including Nobu, Olives by Todd English,  and Fish by JosÃ© AndrÃ©s.&nbsp;
â€¢ Mandara Spa:  Balinese-inspired treatments.
â€¢ Fitness centre:  ocean-view gym.
â€¢ Golf: 18-hole Ocean Club course.
â€¢ Kidsâ€™ programme:  Atlantis Kids Adventures (ages 3â€”12).
</div>

<!-- Google Tag Manager -->
© 2024 Premium Hotels Group  |  Do Not Sell My Info  |  Accessibility  |  Sitemap'''
    },
]

##HOTEL LOCATIONS

LOCATIONS = [
    {
        "hotel_name": "Burj Al Arab",
        "text": '''<div class='location-info'>
<h3>LOCATION â€” Burj Al Arab,  jumeirah, DUBAI</h3>

<p>The Burj Al Arab is located  on an artificial island 280 metres offshore  from Jumeirah Beach.&nbsp;  Connected to the mainland by a private curving bridge,  the hotel sits in the affluent Jumeirah district  of Dubai.</p>

Nearby Attractions:
â€¢ Wild Wadi Waterpark â€” 0.3 km  (complimentary shuttle)
â€¢ Jumeirah Beach â€” adjacent
â€¢ Mall of the Emirates â€” 8 km  (15 min drive)&nbsp;
â€¢ Dubai Mall &amp; Burj Khalifa â€” 18 km  (25 min drive)
â€¢ Dubai International Airport â€” 25 km  (30 min drive)&nbsp;&nbsp;
â€¢ Palm Jumeirah â€” 12 km

<p>The Jumeirah neighbourhood is known  for its pristine beaches, upscale dining,  and luxury villas.  Jumeirah Beach Road is lined with boutique shops,  art galleries, and cafÃ©s.</p>
</div>

© 2024 HotelCorp. All rights reserved. | Privacy Policy | Terms'''
    },
    {
        "hotel_name": "The Ritz London",
        "text": '''location â€” THE RITZ london,  piccadilly

The Ritz London sits at 150 Piccadilly,  one of Londonâ€™s most prestigious addresses.&nbsp;  The hotel overlooks Green Park and is a stoneâ€™s throw from  Mayfair and St. Jamesâ€™s.

<p>Nearby Attractions:</p>
â€¢ Green Park â€” adjacent  (direct views from hotel)
â€¢ Buckingham Palace â€” 0.5 km  (7 min walk)&nbsp;
â€¢ Royal Academy of Arts â€” 0.3 km
â€¢ Fortnum &amp; Mason â€” 0.2 km
â€¢ Piccadilly Circus â€” 0.6 km  (10 min walk)&nbsp;&nbsp;
â€¢ Bond Street shopping â€” 0.8 km
â€¢ Green Park Underground Station  â€” 0.2 km (Piccadilly, Victoria, Jubilee lines)

Piccadilly is one of the widest  and most famous streets in London,  running from Hyde Park Corner  to Piccadilly Circus.&nbsp; The area has been a centre of commerce  and aristocratic residences since the 17th century.

<div class='footer'>© 2024 Luxury Hotels International. All rights reserved. | Privacy Policy | Terms of Service | Cookie Settings</div>'''
    },
    {
        "hotel_name": "Marina Bay Sands",
        "text": '''<div class='location-details'>
LOCATION â€” marina bay sands, singapore

Marina Bay Sands  is situated on the waterfront  along Marina Bay in Singaporeâ€™s  Central Business District.&nbsp;

Nearby Attractions:
â€¢ Gardens by the Bay â€” 0.5 km  (8 min walk)
â€¢ Merlion Park â€” 1 km  (12 min walk)&nbsp;
â€¢ Esplanade Theatres â€” 1.2 km
â€¢ Chinatown â€” 2 km  (5 min by MRT)&nbsp;&nbsp;
â€¢ Orchard Road shopping â€” 3.5 km  (10 min by taxi)
â€¢ Singapore Flyer â€” 1.5 km
â€¢ Changi Airport â€” 20 km  (25 min drive)

<p>Transport Links:  Bayfront MRT Station (Circle Line &amp; Downtown Line)  is directly connected to the hotel  via underground walkway.&nbsp; The CBD location makes it ideal  for both business and leisure travellers.</p>
</div>

This page was last updated on 2024-03-15.&nbsp;&nbsp;© HotelReviews.com&nbsp;|&nbsp;About Us&nbsp;|&nbsp;Contact'''
    },
    {
        "hotel_name": "Waldorf Astoria New York",
        "text": '''Location â€” WALDORF ASTORIA  new york,  park avenue

<p>The Waldorf Astoria occupies  an entire city block on Park Avenue  between 49th and 50th Streets  in midtown Manhattan.&nbsp;&nbsp;</p>

Nearby Attractions:
â€¢ Grand Central Terminal â€” 0.3 km  (5 min walk)
â€¢ Rockefeller Center â€” 0.5 km  (8 min walk)&nbsp;
â€¢ St. Patrickâ€™s Cathedral â€” 0.4 km
â€¢ Times Square â€” 1 km  (15 min walk)
â€¢ Central Park â€” 1.2 km  (18 min walk)&nbsp;&nbsp;
â€¢ Empire State Building â€” 1.5 km
â€¢ JFK Airport â€” 27 km  (45â€”90 min depending on traffic)

Park Avenue is one of  the most prestigious addresses  in the world.&nbsp;  The midtown location places guests  within walking distance of major  corporate offices, museums, theatres,  and shopping on Fifth Avenue.

<p class='disclaimer'>The information on this page is provided â€œas isâ€\x9d without warranty. Prices and availability subject to change.</p>
© 2024 TravelInfo Ltd. | GDPR | Sitemap'''
    },
    {
        "hotel_name": "The Peninsula Hong Kong",
        "text": '''<div>
LOCATION â€” the peninsula hong kong,  tsim sha tsui

The Peninsula Hong Kong  is located on Salisbury Road  in the heart of Tsim Sha Tsui,  Kowloonâ€™s premier commercial  and tourist district.&nbsp;

Nearby Attractions:
â€¢ Victoria Harbour  waterfront promenade â€” adjacent
â€¢ Hong Kong Cultural Centre â€” 0.2 km&nbsp;
â€¢ Star Ferry Pier â€” 0.3 km  (5 min walk to Hong Kong Island)
â€¢ Avenue of Stars â€” 0.5 km&nbsp;&nbsp;
â€¢ Temple Street Night Market â€” 1.5 km
â€¢ Hong Kong International Airport â€” 34 km  (Peninsula helicopter: 12 min)

<p>Transport: Tsim Sha Tsui MTR Station  is 0.3 km away, providing direct access  to Hong Kong Island via the Tsuen Wan Line.&nbsp; The Cross-Harbour Tunnel  connects Kowloon to Central  in under 10 minutes by taxi.</p>
</div>

---\nPowered by HotelStack CMS v3.2.1 | Page generated in 0.034s\n<script>var analytics='UA-000000-1';</script>'''
    },
    {
        "hotel_name": "Hotel del Coronado",
        "text": '''location â€” HOTEL DEL CORONADO,  coronado, california

The Hotel del Coronado sits  on the white sand shores of Coronado Beach  on the Coronado Peninsula,&nbsp;  connected to downtown San Diego  by the Coronado Bridge.

<p>Nearby Attractions:</p>
â€¢ Coronado Beach â€” adjacent
â€¢ Coronado Ferry Landing â€” 2 km  (ferry to San Diego downtown)&nbsp;
â€¢ San Diego Zoo â€” 10 km  (20 min drive)
â€¢ Gaslamp Quarter â€” 8 km  (15 min drive)&nbsp;&nbsp;
â€¢ USS Midway Museum â€” 7 km
â€¢ LEGOLAND California â€” 50 km  (45 min drive)
â€¢ San Diego International Airport  â€” 6 km (15 min drive)

Coronado is a resort city  known for its mild year-round climate,  tree-lined streets, and relaxed  beach-town atmosphere.&nbsp;  The Orange Avenue shopping district  is a 5-minute walk from  the hotel.

<footer>
<nav>Home | About | Hotels | Reviews | Contact Us</nav>
<p>© 2023-2024 StayGuide Inc. All rights reserved.</p>
</footer>'''
    },
    {
        "hotel_name": "Atlantis Paradise Island",
        "text": '''<div class='location-page'>
LOCATION â€” atlantis paradise island,  nassau, BAHAMAS

Atlantis Paradise Island  is located on Paradise Island,  connected to Nassau (the capital)  by two bridges.&nbsp;&nbsp;

Nearby Attractions:
â€¢ Cabbage Beach â€” adjacent
â€¢ Nassau Straw Market â€” 3 km  (across the bridge)&nbsp;
â€¢ Fort Charlotte â€” 5 km
â€¢ Blue Lagoon Island â€” 5 km  (boat excursion)
â€¢ Ardastra Gardens â€” 6 km&nbsp;&nbsp;
â€¢ Lynden Pindling International Airport  â€” 20 km (30 min drive)

<p>Paradise Island is a 2.7 km  barrier island  in the Bahamas. &nbsp; Once known as Hogâ€™s Island,  it was renamed in the 1960s  and developed into  a world-class resort destination.  The island offers  turquoise waters, coral reefs,  and year-round tropical weather  (average temperature 25â€”32Â°C).</p>
</div>

<!-- Google Tag Manager -->
© 2024 Premium Hotels Group  |  Do Not Sell My Info  |  Accessibility  |  Sitemap'''
    },
]


def generate_all_files():
    """Write each messy document as an individual .txt file in data/raw/."""
    out_dir = os.path.join("data", "raw")
    os.makedirs(out_dir, exist_ok=True)

    categories = [
        ("description", DESCRIPTIONS),
        ("review", REVIEWS),
        ("policy", POLICIES),
        ("amenities", AMENITIES),
        ("location", LOCATIONS),
    ]

    total_files = 0
    counters = Counter()
    hotel_counters = Counter()
    review_indices = {}

    for cat_name, items in categories:
        for item in items:
            hotel_name = item["hotel_name"]
            text_content = item["text"]

            
            hotel_slug = clean_filename(hotel_name)
            
            if cat_name == "review":
                review_indices[hotel_slug] = review_indices.get(hotel_slug, 0) + 1
                filename = f"{hotel_slug}_review_{review_indices[hotel_slug]}.txt"
            else:
                filename = f"{hotel_slug}_{cat_name}.txt"

            full_path = os.path.join(out_dir, filename)
            with open(full_path, "w", encoding="utf-8") as fh:
                fh.write(text_content)

            total_files += 1
            counters[cat_name] += 1
            hotel_counters[hotel_name] += 1

    print(f"\nâœ… Successfully generated {total_files} messy text files in '{out_dir}/'!")
    
    print("\n  Category Breakdown:")
    for cat, count in sorted(counters.items()):
        print(f"    - {cat}: {count} files")
        
    print("\n  Hotel Breakdown:")
    for hotel, count in sorted(hotel_counters.items()):
        print(f"    - {hotel}: {count} files")

    all_texts = []
    for cat_name, items in categories:
        for item in items:
            all_texts.append(item["text"])
    combined = " ".join(all_texts)

    print("\n  Messiness Indicators Present in Output:")
    print(f"    - HTML Tags (<p>, <div>, etc.):  {combined.count('<')}")
    print(f"    - &amp; entities:                 {combined.count('&amp;')}")
    print(f"    - &nbsp; entities:                {combined.count('&nbsp;')}")
    print(f"    - â€™ (right single quote):       {combined.count('â€™')}")
    print(f"    - â€” (em-dash mojibake):          {combined.count('â€”')}")
    print(f"    - © footers:                      {combined.count('©')}")
    print(f"    - Double spaces:                  {combined.count('  ')}")

if __name__ == "__main__":
    generate_all_files()
