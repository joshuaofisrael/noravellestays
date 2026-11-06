"""Page data for scripts/best_rooms_page.py. Every specific claim must match a listed source."""

WC = "https://thewindsorcourt.com/rooms/"
PV = "https://www.pontevedra.com/stay/inn-club/rooms-suites"

PAGES = [
  {
    "slug": "windsor-court-new-orleans",
    "hotel": "The Windsor Court",
    "city": "New Orleans",
    "city_url": "/hotels/new-orleans/",
    "official_url": "https://thewindsorcourt.com/",
    "checked": "2026-11-06", "checked_human": "6 November 2026",
    "title": "Best Rooms at The Windsor Court, New Orleans: Which Room to Request",
    "description": "Which room to ask for at The Windsor Court in New Orleans: Guest Rooms vs Deluxe and Premium Suites, Club Level floors 19 to 22, river or skyline views, balconies and how to ask.",
    "quick": f"""<p><strong>For most couples, book a Deluxe Suite and ask for a river view.</strong> The hotel lists Deluxe Suites at 600 square feet with a private balcony, while the 400 square foot Guest Rooms only say that many include a balcony. If lounge breakfast, afternoon tea and evening drinks matter, book Club Level, which the hotel places on floors 19 to 22. Families should look at the Two Bedroom Corner Suite or ask for connecting rooms (<a href="{WC}" rel="noopener noreferrer" target="_blank">official rooms page</a>).</p>""",
    "compare": [
      ("Guest Room", "400 sq ft", "1 king or 2 queens", "River or city skyline", "Many, not all, include a private balcony; sofa bed in many king rooms"),
      ("Deluxe Suite", "600 sq ft", "1 king", "River or city skyline", "Private balcony; dining table or reading chair"),
      ("Premium Suite", "800 sq ft", "1 king or 2 queens", "River or city skyline", "French doors between living area and bedroom; many include a balcony; two bedroom versions available"),
      ("Two Bedroom Corner Suite", "1,250 sq ft", "1 canopy king plus 2 queens", "Not stated", "Club Level; balcony; two full baths; large wet bar"),
      ("Presidential Suite", "2,780 sq ft", "Two bedrooms", "Mississippi River and French Quarter", "22nd floor; private rooftop terraces; private gym"),
    ],
    "floors": f"""<p>The hotel says Club Level occupies <strong>floors 19 to 22</strong>, with a dedicated concierge and a Club Level Lounge serving breakfast, afternoon tea, evening cocktails and nightly desserts. The James J. Coleman, Jr. Presidential Suite is on the 22nd floor. The owner, Crow Holdings, states that all 314 rooms and suites have private balconies or bay windows with Mississippi River or city skyline views (<a href="https://www.crowholdings.com/property/the-windsor-court/" rel="noopener noreferrer" target="_blank">Crow Holdings</a>). So the main choice is which side you face: ask for the river side if the view matters most to you.</p>
        <p>Below Club Level, the hotel does not publish which floors face which way. A higher floor on the river side is a sensible request, but it is a request, not a published room plan.</p>""",
    "request": [
      "<strong>Deluxe Suite, river view:</strong> the smallest category the hotel lists with a private balcony on every unit.",
      "<strong>Club Level (floors 19 to 22):</strong> for the lounge and the highest floors the hotel names.",
      "<strong>Two Bedroom Corner Suite:</strong> for families or two couples who want one key, two bathrooms and a balcony.",
      "<strong>Connecting rooms:</strong> the hotel says many Deluxe and Premium Suites connect to adjoining Guest Rooms or suites.",
    ],
    "avoid": [
      "<strong>A Guest Room if a balcony is the point:</strong> the hotel says many Guest Rooms include a balcony, not all. Book a Deluxe Suite or confirm a balcony in writing.",
      "<strong>A city skyline room if you came for the river:</strong> both outlooks exist, so ask for the river side when you book and again at check in.",
      "<strong>Noise:</strong> the hotel describes double paned windows and a quieter setting just beyond the French Quarter, and we found no published list of noisy rooms. If you are a light sleeper, ask for a room away from elevators and service areas.",
    ],
    "ask": [
      "<strong>At booking:</strong> book the category that guarantees what you care about (a Deluxe Suite for a balcony, Club Level for floors 19 to 22). Add a note: \"High floor, river view, balcony please.\"",
      "<strong>By phone:</strong> the hotel asks guests to call reservations at (888) 596 0955 for specific room inventory and accessibility details.",
      "<strong>Accessibility:</strong> ADA rooms include roll in showers, grab bars and visual alerts; tell reservations what you need.",
      "<strong>At check in:</strong> ask politely whether a river view room on a higher floor is open in your category before you take the key.",
    ],
    "faq": [
      ("What is the best room at The Windsor Court?", "For most couples, a Deluxe Suite with a river view. The hotel lists it at 600 square feet with a private balcony. For more space or a lounge, look at Premium Suites or Club Level on floors 19 to 22."),
      ("Which floors are Club Level at The Windsor Court?", "The hotel says Club Level occupies floors 19 through 22, with a dedicated concierge and a Club Level Lounge."),
      ("Do all rooms at The Windsor Court have a balcony?", "No. The hotel says many Guest Rooms and many Premium Suites include a private balcony, while Deluxe Suites list a private balcony. The owner says every room has either a balcony or a bay window."),
      ("Can I request a river view at The Windsor Court?", "Yes, you can ask. Rooms face either the Mississippi River or the city skyline. A request is not a guarantee, so confirm the view in writing if it matters."),
    ],
    "sources": [
      ("The Windsor Court: Rooms and Suites (official)", WC),
      ("The Windsor Court: Guest Rooms (official)", "https://thewindsorcourt.com/rooms/guest-room/"),
      ("The Windsor Court: Premium Suites (official)", "https://thewindsorcourt.com/rooms/premium-suite/"),
      ("Crow Holdings: The Windsor Court property page (owner)", "https://www.crowholdings.com/property/the-windsor-court/"),
    ],
  },
  {
    "slug": "ponte-vedra-inn-and-club",
    "hotel": "Ponte Vedra Inn & Club",
    "city": "Jacksonville and Ponte Vedra Beach",
    "city_url": "/hotels/jacksonville/",
    "official_url": "https://www.pontevedra.com/stay/inn-club",
    "checked": "2026-11-06", "checked_human": "6 November 2026",
    "title": "Best Rooms at Ponte Vedra Inn & Club: Which Room to Request",
    "description": "Which room to ask for at Ponte Vedra Inn & Club: Superior Oceanfront vs Preferred Oceanfront vs Beachside, Historic Inn and Island View rooms, the Penthouse Suite and how to ask.",
    "quick": f"""<p><strong>Book a Superior Oceanfront room if the ocean view is why you are going.</strong> The resort calls these its newest and most popular rooms, with unobstructed panoramic Atlantic views and a balcony or patio directly on the beach. A Preferred Oceanfront room also faces the ocean and adds a kitchenette. Avoid the Beachside categories if you want a full sea view: the resort says Preferred Beachside rooms have limited or no ocean views (<a href="{PV}" rel="noopener noreferrer" target="_blank">official rooms page</a>).</p>""",
    "compare": [
      ("Superior Oceanfront", "Not stated", "1 king or 2 queens", "Unobstructed panoramic ocean", "Newest and most popular per the resort; balcony or patio on the beach; soaking tub, many beside sliding doors"),
      ("Superior Oceanfront Suite", "Not stated", "1 king", "Oceanfront", "Balcony or terrace; up to 5 guests"),
      ("Preferred Oceanfront", "Not stated", "1 king or 2 queens", "Ocean view from balcony or patio", "Kitchenette; connecting rooms; parking near the room"),
      ("Superior Beachside", "Not stated", "1 king", "Side ocean view", "Up to 3 guests; balcony or terrace"),
      ("Preferred Beachside", "Not stated", "1 king or 2 queens", "Limited or no ocean view", "Close to the beach; kitchenette"),
      ("Historic Inn Room", "Not stated", "1 king or 2 queens", "Resort or lagoon", "Above the Great Lounge and lobby; balcony"),
      ("Island View Room", "Not stated", "1 king or 2 queens", "Inland lagoons and the 9th Island Hole", "Island House; balcony or terrace"),
      ("Penthouse Suite", "Not stated", "1 king", "Ocean and the signature fountain", "High atop the Inn; private elevator access"),
      ("Presidential Suite", "Not stated", "1 king", "Panoramic ocean", "Two at the resort; patio or balcony"),
    ],
    "floors": f"""<p>The resort describes itself as ten low rise buildings with 262 rooms and suites, so <strong>the building and the outlook matter more than the floor</strong>. Ocean views come with the Oceanfront categories; the Historic Inn rooms look over the resort or the lagoon; Island House rooms look over the lagoons and the golf course. The one high room the resort names is the Penthouse Suite, which it places high atop the Inn with private elevator access.</p>
        <p>The resort map lists the Atlantic House, Ocean House, Beach House and other buildings, but the official pages do not say which room types sit in which building, so we do not guess.</p>""",
    "request": [
      "<strong>Superior Oceanfront:</strong> for unobstructed ocean views and a balcony or patio on the beach.",
      "<strong>Preferred Oceanfront:</strong> for an ocean view plus a kitchenette, or connecting rooms for a family.",
      "<strong>Penthouse Suite:</strong> the top room at the Inn, with ocean and fountain views.",
      "<strong>Island View or Historic Inn:</strong> if you prefer a lagoon or golf outlook to the beach.",
    ],
    "avoid": [
      "<strong>Preferred Beachside, if you want a sea view:</strong> the resort itself says limited or no ocean views.",
      "<strong>Superior Beachside, if you want a straight on view:</strong> the resort describes side views of the ocean.",
      "<strong>Island View or Historic Inn rooms for a beach view:</strong> these face the lagoon, the golf course or the resort, per the resort.",
      "<strong>Noise:</strong> Historic Inn rooms sit above the Great Lounge and lobby, per the resort. If you are a light sleeper, ask whether your room is directly over a public space. We found no published list of noisy rooms.",
    ],
    "ask": [
      "<strong>At booking:</strong> choose the category that guarantees the view. A request note will not turn a Beachside booking into an Oceanfront room.",
      "<strong>By phone:</strong> resort reservations are listed at (888) 839 9145; ask which building your category is in.",
      "<strong>Families:</strong> Preferred Oceanfront and Superior Oceanfront rooms list connecting rooms; request them when you book.",
      "<strong>At check in:</strong> ask whether a room with a balcony directly on the beach is open in your category.",
    ],
    "faq": [
      ("What is the best room at Ponte Vedra Inn & Club?", "For most guests, a Superior Oceanfront room. The resort calls it the newest and most popular room, with unobstructed panoramic ocean views and a balcony or patio directly on the beach."),
      ("Which rooms at Ponte Vedra Inn & Club do not have an ocean view?", "The resort says Preferred Beachside rooms have limited or no ocean views. Historic Inn rooms face the resort or lagoon, and Island View rooms face the lagoons and golf course."),
      ("Does Ponte Vedra Inn & Club have connecting rooms?", "Yes. The resort lists connecting rooms for Preferred Oceanfront and Superior Oceanfront rooms. Request them when you book."),
      ("Where is the Penthouse Suite at Ponte Vedra Inn & Club?", "The resort says it is high atop the Inn, with private elevator access and views of the ocean and the signature fountain."),
    ],
    "sources": [
      ("Ponte Vedra Inn & Club: Rooms and Suites (official)", PV),
      ("Ponte Vedra Inn & Club: Superior Oceanfront (official)", "https://www.pontevedra.com/stay/inn-club/rooms-suites/superior-oceanfront"),
      ("Ponte Vedra Inn & Club: Preferred Oceanfront Room (official)", "https://www.pontevedra.com/stay/inn-club/rooms-suites/preferred-oceanfront-room"),
      ("Ponte Vedra Inn & Club: resort overview and map (official)", "https://www.pontevedra.com/stay/inn-club"),
    ],
  },
]
