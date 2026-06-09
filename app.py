import streamlit as st

st.set_page_config(
    page_title="StageScape",
    page_icon="🎤",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background:
    radial-gradient(circle at 10% 5%, rgba(255, 0, 150, 0.28), transparent 28%),
    radial-gradient(circle at 90% 10%, rgba(0, 200, 255, 0.22), transparent 30%),
    radial-gradient(circle at 50% 100%, rgba(140, 80, 255, 0.24), transparent 35%),
    #050509;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

h1, h2, h3, h4, p, li, label {
    color: white !important;
}

[data-testid="stMarkdownContainer"] {
    color: white !important;
}

button {
    font-weight: 700 !important;
}

button[data-baseweb="tab"] p {
    color: white !important;
    font-weight: 700 !important;
}

button[data-baseweb="tab"][aria-selected="true"] p {
    color: #ff5ac8 !important;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 20px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)


def case(artist, title, venue, scale, audience, year, production, tags, analysis, link):
    return {
        "artist": artist,
        "title": title,
        "venue": venue,
        "scale": scale,
        "audience": audience,
        "year": year,
        "production": production,
        "tags": tags,
        "analysis": analysis,
        "visual_link": link
    }


concerts = [
    case("BTS", "Permission To Dance On Stage", "SoFi Stadium / Olympic Stadium", "Mega Stadium", "50,000+", "2021–2022", "HYBE Production", ["LED Wall", "Projection Mapping", "Automated Lift", "Moving Runway"], "Stadium-scale LED screens and extended runways were used to keep the performance visible and immersive across a very large venue.", "https://www.youtube.com/results?search_query=BTS+Permission+To+Dance+On+Stage+concert"),
    case("BTS", "Love Yourself: Speak Yourself", "Wembley Stadium / Global Stadiums", "World Stadium Tour", "60,000+", "2019", "Big Hit Production", ["LED Wall", "Pyrotechnics", "Moving Runway", "Laser System"], "A stadium-scale tour using large LED architecture, fireworks, and extended stage routes to connect with distant audience sections.", "https://www.youtube.com/results?search_query=BTS+Speak+Yourself+Wembley+stage"),
    case("BLACKPINK", "BORN PINK WORLD TOUR", "Gocheok Sky Dome / Global Stadiums", "World Stadium Tour", "55,000+", "2022–2023", "YG Stage Team", ["LED Wall", "Kinetic Stage", "Laser System", "Drone Show"], "The tour used bold LED visuals, strong lighting contrast, and moving stage structures to create a luxury-pop concert identity.", "https://www.youtube.com/results?search_query=BLACKPINK+BORN+PINK+WORLD+TOUR+stage"),
    case("BLACKPINK", "IN YOUR AREA WORLD TOUR", "Global Arenas", "World Arena Tour", "10,000–20,000", "2018–2020", "YG Entertainment", ["LED Wall", "Laser System", "Moving Runway"], "Arena-scale screens and runways supported the group’s strong performance identity and direct audience interaction.", "https://www.youtube.com/results?search_query=BLACKPINK+IN+YOUR+AREA+concert+stage"),
    case("BIGBANG", "MADE WORLD TOUR", "Olympic Gymnastics Arena / Global Arenas", "World Tour", "Large Arena", "2015–2016", "YG Entertainment", ["LED Wall", "Kinetic Stage", "Laser System"], "A bold arena concert structure built around large video screens, band-like performance energy, and dramatic light transitions.", "https://www.youtube.com/results?search_query=BIGBANG+MADE+Tour+stage"),
    case("G-DRAGON", "ACT III: M.O.T.T.E", "World Tour Arenas", "Solo World Tour", "Large Arena", "2017", "YG Entertainment", ["LED Wall", "Projection Mapping", "Laser System"], "A highly art-directed solo concert using symbolic visuals, intense red lighting, and theatrical screen imagery.", "https://www.youtube.com/results?search_query=G-DRAGON+MOTTE+concert+stage"),
    case("aespa", "SYNK: HYPER LINE", "KSPO Dome", "Arena Tour", "15,000+", "2023", "SM Visual Production", ["XR", "AR Camera", "LED Wall", "Virtual Production"], "The concert connects aespa’s virtual-world concept with avatar-like visuals, immersive LED environments, and camera-based digital effects.", "https://www.youtube.com/results?search_query=aespa+SYNK+HYPER+LINE+concert+stage"),
    case("aespa", "SYNK: PARALLEL LINE", "Jamsil Indoor Stadium / Global Arenas", "Arena Tour", "10,000+", "2024", "SM Visual Production", ["XR", "LED Wall", "AR Camera", "Laser System"], "A performance system continuing aespa’s digital-world identity through layered LED space, cyber visuals, and camera-based effects.", "https://www.youtube.com/results?search_query=aespa+SYNK+PARALLEL+LINE+concert+stage"),
    case("NCT 127", "NEO CITY: THE LINK", "Tokyo Dome / KSPO Dome", "Dome Tour", "50,000+", "2022–2023", "SM Stage Division", ["XR", "Kinetic Stage", "LED Wall", "Laser System"], "Cyberpunk-inspired visuals, modular stage construction, and intense lighting systems created a futuristic concert identity.", "https://www.youtube.com/results?search_query=NCT+127+NEO+CITY+THE+LINK+concert+stage"),
    case("NCT DREAM", "THE DREAM SHOW 2", "Jamsil Olympic Stadium / Global Arenas", "Stadium / Arena Tour", "30,000+", "2022–2023", "SM Entertainment", ["LED Wall", "Moving Runway", "Confetti System", "Laser System"], "Large LED screens and extended stage routes support youthful energy and high audience contact across a large venue.", "https://www.youtube.com/results?search_query=NCT+DREAM+THE+DREAM+SHOW+2+stage"),
    case("NCT DREAM", "THE DREAM SHOW 3", "Gocheok Sky Dome / Global Arenas", "Dome / Arena Tour", "20,000+", "2024", "SM Entertainment", ["LED Wall", "Kinetic Stage", "Laser System"], "A dome-scale visual system built around bright LED graphics, large stage depth, and synchronized light movement.", "https://www.youtube.com/results?search_query=NCT+DREAM+THE+DREAM+SHOW+3+stage"),
    case("EXO", "EXO PLANET #2: The EXO'luxion", "Olympic Gymnastics Arena / Global Arenas", "Arena Tour", "15,000+", "2015–2016", "SM Entertainment", ["Hologram", "LED Wall", "Projection Mapping", "Moving Runway"], "Earlier large-scale K-pop touring used hologram-like effects, theatrical VCRs, and fantasy stage environments.", "https://www.youtube.com/results?search_query=EXO+PLANET+EXOluxion+hologram+stage"),
    case("SHINee", "SHINee WORLD VI: PERFECT ILLUMINATION", "KSPO Dome / Tokyo Dome", "Arena / Dome Tour", "15,000–50,000", "2023–2024", "SM Entertainment", ["LED Wall", "Laser System", "Moving Runway", "Follow Spot System"], "Lighting design plays a central role, supporting SHINee’s performance identity with precise spotlights and elegant screen visuals.", "https://www.youtube.com/results?search_query=SHINee+PERFECT+ILLUMINATION+concert+stage"),
    case("Red Velvet", "R to V", "KSPO Dome / Global Venues", "Arena Tour", "10,000+", "2023", "SM Entertainment", ["LED Wall", "Projection Mapping", "Theatrical Set"], "A concept-driven show using contrasting visual worlds, scenic set changes, and screen graphics to reflect dual identities.", "https://www.youtube.com/results?search_query=Red+Velvet+R+to+V+concert+stage"),
    case("SEVENTEEN", "FOLLOW TOUR", "Seoul / Tokyo Dome", "Dome Tour", "45,000+", "2023–2024", "PLEDIS Production", ["LED Wall", "Kinetic Stage", "Automated Lift", "Moving Runway"], "Extended stage architecture and moving platforms support group choreography while increasing audience connection in large dome venues.", "https://www.youtube.com/results?search_query=SEVENTEEN+FOLLOW+TOUR+stage"),
    case("SEVENTEEN", "BE THE SUN", "Gocheok Sky Dome / Global Arenas", "World Arena Tour", "20,000+", "2022", "PLEDIS Production", ["LED Wall", "Laser System", "Moving Runway"], "A bright and powerful concert design using large LED screens and runways to support high-energy group choreography.", "https://www.youtube.com/results?search_query=SEVENTEEN+BE+THE+SUN+concert+stage"),
    case("TXT", "ACT: SWEET MIRAGE", "KSPO Dome / Global Arenas", "Arena Tour", "15,000+", "2023", "HYBE Production", ["Projection Mapping", "LED Wall", "Automated Lift", "Theatrical Set"], "Fantasy-like visual direction is supported through scenic LED imagery, theatrical transitions, and layered stage space.", "https://www.youtube.com/results?search_query=TXT+ACT+SWEET+MIRAGE+stage"),
    case("TXT", "ACT: PROMISE", "KSPO Dome / Global Arenas", "Arena Tour", "15,000+", "2024", "HYBE Production", ["LED Wall", "Projection Mapping", "Moving Runway"], "A narrative-driven arena show using wide LED compositions and scenic transitions to connect performances into a fantasy journey.", "https://www.youtube.com/results?search_query=TXT+ACT+PROMISE+concert+stage"),
    case("ENHYPEN", "FATE Tour", "KSPO Dome / Global Arenas", "Arena Tour", "15,000+", "2023–2024", "BELIFT / HYBE", ["LED Wall", "Projection Mapping", "Kinetic Stage", "Laser System"], "Dark fantasy visuals and moving stage structures build a dramatic narrative-oriented concert atmosphere.", "https://www.youtube.com/results?search_query=ENHYPEN+FATE+Tour+stage"),
    case("LE SSERAFIM", "FLAME RISES", "Jamsil Indoor Stadium", "Arena Concert", "10,000+", "2023", "Source Music / HYBE", ["LED Wall", "Laser System", "Automated Lift"], "Minimal but powerful stage visuals emphasize choreography, confidence, and strong lighting contrast.", "https://www.youtube.com/results?search_query=LE+SSERAFIM+FLAME+RISES+concert+stage"),
    case("NewJeans", "Lollapalooza / Bunnies Camp", "Festival Stage / Fan Meeting Venue", "Festival / Fan Meeting", "Large Festival", "2023–2024", "ADOR", ["LED Wall", "Projection Mapping", "Graphic Screen Design"], "Clean graphic visuals and retro-inspired screen design support the group’s casual and nostalgic visual identity.", "https://www.youtube.com/results?search_query=NewJeans+Lollapalooza+stage"),
    case("Stray Kids", "MANIAC / 5-STAR Tour", "KSPO Dome / Global Arenas", "Arena Tour", "15,000–40,000", "2022–2024", "JYP Production", ["LED Wall", "Laser System", "Kinetic Stage", "Pyrotechnics"], "Sharp lighting, industrial video design, and powerful LED environments match the group’s intense performance style.", "https://www.youtube.com/results?search_query=Stray+Kids+MANIAC+concert+stage"),
    case("Stray Kids", "dominATE World Tour", "Global Stadiums / Arenas", "World Tour", "Large Arena / Stadium", "2024–2025", "JYP Production", ["LED Wall", "Laser System", "Moving Runway", "Pyrotechnics"], "A larger tour format emphasizing aggressive lighting, stadium visibility, and high-impact performance moments.", "https://www.youtube.com/results?search_query=Stray+Kids+dominATE+world+tour+stage"),
    case("TWICE", "READY TO BE", "KSPO Dome / Global Stadiums", "World Stadium Tour", "40,000+", "2023–2024", "JYP Production", ["LED Wall", "Kinetic Stage", "Automated Lift", "Moving Runway"], "A bright pop concert system designed for member movement, large audience visibility, and colorful screen-based production.", "https://www.youtube.com/results?search_query=TWICE+READY+TO+BE+concert+stage"),
    case("ITZY", "BORN TO BE Tour", "Jamsil Indoor Stadium / Global Venues", "World Tour", "10,000+", "2024", "JYP Production", ["LED Wall", "Laser System", "Automated Lift"], "A more intense stage identity built through dark lighting, powerful screen graphics, and choreographic focus.", "https://www.youtube.com/results?search_query=ITZY+BORN+TO+BE+concert+stage"),
    case("NMIXX", "NICE TO MIXX YOU", "Theater / Arena Venues", "Showcase Tour", "Small–Mid Venue", "2023", "JYP Production", ["LED Wall", "Graphic Screen Design", "Follow Spot System"], "Compact tour staging uses graphic LED visuals and clean lighting to support live vocals and performance transitions.", "https://www.youtube.com/results?search_query=NMIXX+NICE+TO+MIXX+YOU+stage"),
    case("IVE", "SHOW WHAT I HAVE", "KSPO Dome / Global Arenas", "Arena Tour", "15,000+", "2023–2024", "Starship Entertainment", ["LED Wall", "Automated Lift", "Projection Mapping"], "Elegant large-screen visuals and vertical stage composition reinforce the group’s polished performance image.", "https://www.youtube.com/results?search_query=IVE+SHOW+WHAT+I+HAVE+concert+stage"),
    case("MONSTA X", "NO LIMIT Tour", "Global Arenas", "World Tour", "Large Arena", "2022", "Starship Entertainment", ["LED Wall", "Laser System", "Pyrotechnics"], "Strong lighting, large screens, and explosive effects support a powerful performance-centered concert image.", "https://www.youtube.com/results?search_query=MONSTA+X+NO+LIMIT+concert+stage"),
    case("IU", "The Golden Hour", "Olympic Stadium", "Stadium Concert", "45,000+ per day", "2022", "EDAM Production", ["Drone Show", "Projection Mapping", "LED Wall", "Follow Spot System"], "Drone visuals, warm lighting, and poetic stadium-scale screen design created an emotional visual narrative.", "https://www.youtube.com/results?search_query=IU+The+Golden+Hour+concert+drone+show"),
    case("TAEMIN", "METAMORPH", "Inspire Arena", "Arena Concert", "10,000+", "2023", "SM Entertainment", ["Kinetic Stage", "LED Wall", "Laser System", "Theatrical Set"], "A performance-art-oriented concert using dramatic structures, controlled lighting, and choreographic staging.", "https://www.youtube.com/results?search_query=TAEMIN+METAMORPH+concert+stage"),
    case("TAEYEON", "The ODD Of LOVE", "KSPO Dome / Asia Venues", "Arena Tour", "10,000+", "2023", "SM Entertainment", ["LED Wall", "Projection Mapping", "Follow Spot System"], "A vocal-centered concert where lighting and screen imagery create mood shifts without overpowering the performer.", "https://www.youtube.com/results?search_query=TAEYEON+The+ODD+Of+LOVE+concert+stage"),
    case("MAMA Awards", "MAMA Awards Stage", "Kyocera Dome / Tokyo Dome", "Award Ceremony", "40,000+", "2023–2024", "CJ ENM", ["XR", "Projection Mapping", "AR Camera", "LED Wall", "Virtual Production"], "Award-show staging combines broadcast XR, camera effects, large LED backdrops, and fast-changing performance sets.", "https://www.youtube.com/results?search_query=MAMA+Awards+XR+stage+performance"),
    case("Melon Music Awards", "MMA Stage", "Inspire Arena / Gocheok Sky Dome", "Award Ceremony", "Large Arena", "2022–2024", "Kakao / Melon", ["LED Wall", "Projection Mapping", "AR Camera"], "Broadcast-focused stage design uses large LED systems and camera effects to highlight individual artist concepts.", "https://www.youtube.com/results?search_query=Melon+Music+Awards+stage+performance"),
    case("SBS Gayo Daejeon", "SBS Gayo Daejeon Stage", "Inspire Arena / Gocheok Sky Dome", "Broadcast Festival", "Large Arena", "2022–2024", "SBS", ["LED Wall", "AR Camera", "Projection Mapping", "Laser System"], "Broadcast-oriented production combines large LED screens, camera movement, and quick scenic changes between teams.", "https://www.youtube.com/results?search_query=SBS+Gayo+Daejeon+stage+performance"),
    case("SMTOWN", "SMTOWN LIVE", "Suwon World Cup Stadium / Tokyo Dome", "Family Concert / Stadium", "40,000+", "2022–2024", "SM Entertainment", ["LED Wall", "Moving Runway", "Laser System", "Pyrotechnics"], "A large label-family concert format requiring flexible stage systems for many artists and quick performance transitions.", "https://www.youtube.com/results?search_query=SMTOWN+LIVE+concert+stage"),
    case("KCON", "KCON Stage", "LA / Japan / Global Arenas", "Convention Concert", "Large Arena", "2022–2024", "CJ ENM", ["LED Wall", "AR Camera", "Projection Mapping", "Graphic Screen Design"], "Convention concert staging uses modular production and strong screen branding to support many artists in one program.", "https://www.youtube.com/results?search_query=KCON+concert+stage+performance"),
    case("Dream Concert", "Dream Concert Stage", "Seoul World Cup Stadium / Large Venues", "Multi-Artist Stadium Event", "40,000+", "2015–2024", "Korea Entertainment Producers Association", ["LED Wall", "Moving Runway", "Pyrotechnics", "Follow Spot System"], "A mass multi-artist event format built around visibility, fast turnovers, and large stadium audience communication.", "https://www.youtube.com/results?search_query=Dream+Concert+Kpop+stage"),
    case("Coachella", "K-pop Festival Stages", "Coachella Stage", "Outdoor Festival", "Large Festival", "2019–2024", "Festival Production", ["LED Wall", "Laser System", "Projection Mapping", "Pyrotechnics"], "Outdoor festival staging emphasizes strong screen visibility, simplified scenic structure, and broadcast impact.", "https://www.youtube.com/results?search_query=Kpop+Coachella+stage+performance"),
    case("Lollapalooza", "K-pop Festival Performances", "Grant Park / Festival Stage", "Outdoor Festival", "Large Festival", "2022–2024", "Festival Production", ["LED Wall", "Laser System", "Graphic Screen Design"], "Festival stages rely on wide LED visibility and strong visual branding that can communicate quickly to mixed audiences.", "https://www.youtube.com/results?search_query=Kpop+Lollapalooza+stage+performance"),
    case("Summer Sonic", "K-pop Festival Stages", "Japan Festival Stages", "Outdoor / Indoor Festival", "Large Festival", "2022–2024", "Festival Production", ["LED Wall", "Laser System", "Follow Spot System"], "Festival staging focuses on flexible lighting, clean screen visuals, and fast setup for multiple artist lineups.", "https://www.youtube.com/results?search_query=Kpop+Summer+Sonic+stage"),
]

all_tags = sorted(set(tag for concert in concerts for tag in concert["tags"]))


def tag_buttons(key):
    if key not in st.session_state:
        st.session_state[key] = "All"

    options = ["All"] + all_tags
    cols = st.columns(4)

    for i, option in enumerate(options):
        with cols[i % 4]:
            if st.button(option, key=f"{key}_{option}", use_container_width=True):
                st.session_state[key] = option

    st.write(f"Selected: **{st.session_state[key]}**")
    return st.session_state[key]


def render_visual(concert):
    st.info(f"🎤 {concert['artist']} — {concert['title']}")


def render_card(concert):
    with st.container(border=True):
        render_visual(concert)
        st.subheader(concert["title"])
        st.write(f"**Artist / Event** — {concert['artist']}")
        st.write(f"**Venue** — {concert['venue']}")
        st.write(f"**Scale** — {concert['scale']}")
        st.write(f"**Audience** — {concert['audience']}")
        st.write(f"**Year** — {concert['year']}")
        st.write(f"**Production** — {concert['production']}")
        st.write("**Technical Analysis**")
        st.write(concert["analysis"])
        st.write("**Technology Tags**")
        st.write(" · ".join(concert["tags"]))
        st.link_button("Open Visual Reference", concert["visual_link"])


st.title("StageScape")
st.subheader("K-pop Concert Technology Visual Archive")
st.write(
    "Explore K-pop concert production through stage technology, venue scale, visual direction, "
    "visual reference links, and performance design systems."
)

tab1, tab2, tab3 = st.tabs([
    "Technology → Concert Analysis",
    "Concert → Technology Analysis",
    "Visual Reference Gallery"
])

with tab1:
    st.header("Explore by Stage Technology")
    selected_tag = tag_buttons("tech_filter")

    if selected_tag == "All":
        filtered = concerts
    else:
        filtered = [concert for concert in concerts if selected_tag in concert["tags"]]

    st.write(f"Showing **{len(filtered)}** concert cases.")

    cols = st.columns(2)
    for idx, concert in enumerate(filtered):
        with cols[idx % 2]:
            render_card(concert)

with tab2:
    st.header("Explore by Concert")

    titles = [concert["title"] for concert in concerts]
    selected_title = st.radio(
        "Select Concert",
        titles,
        horizontal=False,
        key="concert_radio"
    )

    selected_concert = next(concert for concert in concerts if concert["title"] == selected_title)

    render_card(selected_concert)

    st.header("Related Technologies")

    for tag in selected_concert["tags"]:
        related = [
            c["title"]
            for c in concerts
            if tag in c["tags"] and c["title"] != selected_concert["title"]
        ]

        with st.container(border=True):
            st.subheader(tag)
            for title in related[:10]:
                st.write(f"• {title}")

with tab3:
    st.header("Visual Reference Gallery")
    st.write(
        "Each card links to an external visual reference page where the actual concert footage or stage reference can be checked."
    )

    selected_visual_tag = tag_buttons("visual_filter")

    if selected_visual_tag == "All":
        gallery = concerts
    else:
        gallery = [concert for concert in concerts if selected_visual_tag in concert["tags"]]

    cols = st.columns(3)
    for idx, concert in enumerate(gallery):
        with cols[idx % 3]:
            with st.container(border=True):
                render_visual(concert)
                st.subheader(concert["artist"])
                st.write(concert["title"])
                st.write(" · ".join(concert["tags"]))
                st.link_button("Open Visual Reference", concert["visual_link"])

st.divider()

st.header("Technology Timeline")

timeline = [
    ("2015", "LED walls became a standard visual system in arena-scale K-pop concerts."),
    ("2018", "Projection mapping and kinetic stage systems became more common in world tours."),
    ("2020", "Online concerts accelerated XR, virtual production, and camera-based visual effects."),
    ("2022", "Drone shows and stadium-scale visual storytelling became more visible."),
    ("2024", "Award shows and festivals increasingly combined broadcast XR with live stage production.")
]

for year, text in timeline:
    with st.container(border=True):
        st.subheader(year)
        st.write(text)

st.divider()

st.header("Archive Statistics")

s1, s2, s3, s4 = st.columns(4)

s1.metric("Concert Cases", len(concerts))
s2.metric("Technology Tags", len(all_tags))
s3.metric("Artists & Events", len(set(c["artist"] for c in concerts)))
s4.metric("Venue Types", len(set(c["scale"] for c in concerts)))

st.divider()
st.caption("StageScape — K-pop Concert Stage Technology Visual Archive")
