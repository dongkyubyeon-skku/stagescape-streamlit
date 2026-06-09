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
    radial-gradient(circle at 15% 10%, rgba(255, 0, 150, 0.28), transparent 28%),
    radial-gradient(circle at 85% 20%, rgba(0, 190, 255, 0.24), transparent 30%),
    radial-gradient(circle at 50% 90%, rgba(140, 80, 255, 0.24), transparent 35%),
    #050509;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

h1, h2, h3, h4, p, li, label, span, div {
    color: #ffffff !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

[data-testid="stMarkdownContainer"] {
    color: #ffffff !important;
}

.stSelectbox label {
    color: white !important;
    font-weight: 800 !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #111111 !important;
}

div[data-baseweb="popover"] * {
    color: #111111 !important;
}

.hero-box {
    padding: 56px;
    border-radius: 36px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.20);
    box-shadow: 0 30px 80px rgba(0,0,0,0.45);
    backdrop-filter: blur(20px);
    margin-bottom: 32px;
}

.hero-title {
    font-size: 78px;
    font-weight: 950;
    line-height: 0.95;
    letter-spacing: -3px;
}

.hero-subtitle {
    font-size: 22px;
    color: #f0f0f0 !important;
    line-height: 1.7;
    margin-top: 22px;
}

.glow-text {
    background: linear-gradient(90deg, #ffffff, #ff7ad9, #6fdcff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.logo-fallback {
    height: 230px;
    border-radius: 28px;
    background:
    linear-gradient(135deg, rgba(255,0,130,0.9), rgba(0,180,255,0.75)),
    #171717;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 38px;
    font-weight: 950;
    letter-spacing: 1px;
    margin-bottom: 18px;
    border: 1px solid rgba(255,255,255,0.25);
}

.card {
    background: rgba(10,10,18,0.84);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 30px;
    padding: 24px;
    margin-bottom: 28px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.35);
}

.tech-pill {
    display: inline-block;
    background: linear-gradient(135deg, #ff3cac, #784ba0, #2b86c5);
    color: white !important;
    padding: 8px 14px;
    border-radius: 999px;
    margin-right: 8px;
    margin-bottom: 8px;
    font-size: 12px;
    font-weight: 800;
}

.meta-text {
    color: #e8e8e8 !important;
    line-height: 1.7;
}

.analysis-text {
    color: #d8d8d8 !important;
    line-height: 1.8;
}

.stat-box {
    padding: 30px;
    border-radius: 26px;
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.18);
    text-align: center;
}

.stat-number {
    font-size: 42px;
    font-weight: 950;
}

.stat-label {
    color: #d0d0d0 !important;
}
</style>
""", unsafe_allow_html=True)


concerts = [
    {
        "artist": "BTS",
        "title": "Permission To Dance On Stage",
        "logo": "BTS",
        "venue": "SoFi Stadium / Olympic Stadium",
        "scale": "Mega Stadium",
        "audience": "50,000+",
        "year": "2021–2022",
        "production": "HYBE Production",
        "tags": ["LED Wall", "Projection Mapping", "Automated Lift"],
        "analysis": "Stadium-scale LED screens and extended runways were used to keep the performance visible and emotionally immersive across a very large venue.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/BTS_at_the_2019_Melon_Music_Awards.png/640px-BTS_at_the_2019_Melon_Music_Awards.png",
        "visual_link": "https://www.youtube.com/results?search_query=BTS+Permission+To+Dance+On+Stage+concert"
    },
    {
        "artist": "BLACKPINK",
        "title": "BORN PINK WORLD TOUR",
        "logo": "BLACKPINK",
        "venue": "Gocheok Sky Dome / Global Stadiums",
        "scale": "World Stadium Tour",
        "audience": "55,000+",
        "year": "2022–2023",
        "production": "YG Stage Team",
        "tags": ["LED Wall", "Kinetic Stage", "Laser System", "Drone Show"],
        "analysis": "The tour used bold LED visuals, strong lighting contrast, and large moving stage structures to create a luxury-pop concert identity.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Blackpink_in_their_pubg_world.jpg/640px-Blackpink_in_their_pubg_world.jpg",
        "visual_link": "https://www.youtube.com/results?search_query=BLACKPINK+BORN+PINK+WORLD+TOUR+stage"
    },
    {
        "artist": "aespa",
        "title": "SYNK : HYPER LINE",
        "logo": "aespa",
        "venue": "KSPO Dome",
        "scale": "Arena Tour",
        "audience": "15,000+",
        "year": "2023",
        "production": "SM Visual Production",
        "tags": ["XR", "AR Camera", "LED Wall"],
        "analysis": "The concert connects aespa’s virtual-world concept with avatar-like visuals, immersive LED environments, and camera-based digital effects.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Aespa_at_the_2023_Melon_Music_Awards.png/640px-Aespa_at_the_2023_Melon_Music_Awards.png",
        "visual_link": "https://www.youtube.com/results?search_query=aespa+SYNK+HYPER+LINE+concert+stage"
    },
    {
        "artist": "SEVENTEEN",
        "title": "FOLLOW TOUR",
        "logo": "SEVENTEEN",
        "venue": "Seoul / Tokyo Dome",
        "scale": "Dome Tour",
        "audience": "45,000+",
        "year": "2023–2024",
        "production": "PLEDIS Production",
        "tags": ["LED Wall", "Kinetic Stage", "Automated Lift"],
        "analysis": "Extended stage architecture and moving platforms support group choreography while increasing audience connection in large dome venues.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Seventeen_for_Marie_Claire_Korea_2024.png/640px-Seventeen_for_Marie_Claire_Korea_2024.png",
        "visual_link": "https://www.youtube.com/results?search_query=SEVENTEEN+FOLLOW+TOUR+stage"
    },
    {
        "artist": "IU",
        "title": "The Golden Hour",
        "logo": "IU",
        "venue": "Olympic Stadium",
        "scale": "Stadium Concert",
        "audience": "45,000+",
        "year": "2022",
        "production": "EDAM Production",
        "tags": ["Drone Show", "Projection Mapping", "LED Wall"],
        "analysis": "Drone visuals, warm lighting, and poetic stadium-scale screen design created an emotional visual narrative.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/IU_for_Golden_Disc_Awards_2024.png/640px-IU_for_Golden_Disc_Awards_2024.png",
        "visual_link": "https://www.youtube.com/results?search_query=IU+The+Golden+Hour+concert+drone+show"
    },
    {
        "artist": "NCT 127",
        "title": "NEO CITY",
        "logo": "NCT 127",
        "venue": "Tokyo Dome / KSPO Dome",
        "scale": "Dome Tour",
        "audience": "50,000+",
        "year": "2022–2023",
        "production": "SM Stage Division",
        "tags": ["XR", "Kinetic Stage", "LED Wall", "Laser System"],
        "analysis": "Cyberpunk-inspired visuals, modular stage construction, and intense lighting systems created a futuristic concert identity.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/NCT_127_for_Dispatch_White_Day_Special.png/640px-NCT_127_for_Dispatch_White_Day_Special.png",
        "visual_link": "https://www.youtube.com/results?search_query=NCT+127+NEO+CITY+concert+stage"
    },
    {
        "artist": "Stray Kids",
        "title": "MANIAC / 5-STAR Tour",
        "logo": "SKZ",
        "venue": "KSPO Dome / Global Arenas",
        "scale": "Arena Tour",
        "audience": "15,000–40,000",
        "year": "2022–2024",
        "production": "JYP Production",
        "tags": ["LED Wall", "Laser System", "Kinetic Stage"],
        "analysis": "Sharp lighting, industrial video design, and powerful LED environments match the group’s intense performance style.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Stray_Kids_for_Dispatch_White_Day_Special.png/640px-Stray_Kids_for_Dispatch_White_Day_Special.png",
        "visual_link": "https://www.youtube.com/results?search_query=Stray+Kids+MANIAC+concert+stage"
    },
    {
        "artist": "TXT",
        "title": "ACT : SWEET MIRAGE",
        "logo": "TXT",
        "venue": "KSPO Dome / Global Arenas",
        "scale": "Arena Tour",
        "audience": "15,000+",
        "year": "2023",
        "production": "HYBE Production",
        "tags": ["Projection Mapping", "LED Wall", "Automated Lift"],
        "analysis": "Fantasy-like visual direction is supported through scenic LED imagery, theatrical transitions, and layered stage space.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/TXT_at_the_2022_Melon_Music_Awards.png/640px-TXT_at_the_2022_Melon_Music_Awards.png",
        "visual_link": "https://www.youtube.com/results?search_query=TXT+ACT+SWEET+MIRAGE+stage"
    },
    {
        "artist": "ENHYPEN",
        "title": "FATE Tour",
        "logo": "ENHYPEN",
        "venue": "KSPO Dome / Global Arenas",
        "scale": "Arena Tour",
        "audience": "15,000+",
        "year": "2023–2024",
        "production": "BELIFT / HYBE",
        "tags": ["LED Wall", "Projection Mapping", "Kinetic Stage"],
        "analysis": "Dark fantasy visuals and moving stage structures build a dramatic narrative-oriented concert atmosphere.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Enhypen_at_the_2022_Melon_Music_Awards.png/640px-Enhypen_at_the_2022_Melon_Music_Awards.png",
        "visual_link": "https://www.youtube.com/results?search_query=ENHYPEN+FATE+Tour+stage"
    },
    {
        "artist": "LE SSERAFIM",
        "title": "FLAME RISES",
        "logo": "LE SSERAFIM",
        "venue": "Jamsil Indoor Stadium",
        "scale": "Arena Concert",
        "audience": "10,000+",
        "year": "2023",
        "production": "Source Music / HYBE",
        "tags": ["LED Wall", "Laser System", "Automated Lift"],
        "analysis": "Minimal but powerful stage visuals emphasize choreography, confidence, and strong lighting contrast.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Le_Sserafim_for_Dispatch_White_Day_Special.png/640px-Le_Sserafim_for_Dispatch_White_Day_Special.png",
        "visual_link": "https://www.youtube.com/results?search_query=LE+SSERAFIM+FLAME+RISES+concert+stage"
    },
    {
        "artist": "NewJeans",
        "title": "Lollapalooza / Bunnies Camp",
        "logo": "NewJeans",
        "venue": "Festival Stage / Fan Meeting Venue",
        "scale": "Festival / Fan Meeting",
        "audience": "Large Festival",
        "year": "2023–2024",
        "production": "ADOR",
        "tags": ["LED Wall", "Projection Mapping"],
        "analysis": "Clean graphic visuals and retro-inspired screen design support the group’s casual and nostalgic visual identity.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/NewJeans_at_the_2023_Melon_Music_Awards.png/640px-NewJeans_at_the_2023_Melon_Music_Awards.png",
        "visual_link": "https://www.youtube.com/results?search_query=NewJeans+Lollapalooza+stage"
    },
    {
        "artist": "IVE",
        "title": "SHOW WHAT I HAVE",
        "logo": "IVE",
        "venue": "KSPO Dome / Global Arenas",
        "scale": "Arena Tour",
        "audience": "15,000+",
        "year": "2023–2024",
        "production": "Starship Entertainment",
        "tags": ["LED Wall", "Automated Lift", "Projection Mapping"],
        "analysis": "Elegant large-screen visuals and vertical stage composition reinforce the group’s polished performance image.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/IVE_for_Dispatch_White_Day_Special.png/640px-IVE_for_Dispatch_White_Day_Special.png",
        "visual_link": "https://www.youtube.com/results?search_query=IVE+SHOW+WHAT+I+HAVE+concert+stage"
    },
    {
        "artist": "TWICE",
        "title": "READY TO BE",
        "logo": "TWICE",
        "venue": "KSPO Dome / Stadiums",
        "scale": "World Stadium Tour",
        "audience": "40,000+",
        "year": "2023–2024",
        "production": "JYP Production",
        "tags": ["LED Wall", "Kinetic Stage", "Automated Lift"],
        "analysis": "A bright pop concert system designed for member movement, large audience visibility, and colorful screen-based production.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Twice_for_Marie_Claire_Korea_2024.png/640px-Twice_for_Marie_Claire_Korea_2024.png",
        "visual_link": "https://www.youtube.com/results?search_query=TWICE+READY+TO+BE+concert+stage"
    },
    {
        "artist": "MAMA Awards",
        "title": "MAMA Awards Stage",
        "logo": "MAMA",
        "venue": "Kyocera Dome / Tokyo Dome",
        "scale": "Award Ceremony",
        "audience": "40,000+",
        "year": "2023–2024",
        "production": "CJ ENM",
        "tags": ["XR", "Projection Mapping", "AR Camera", "LED Wall"],
        "analysis": "Award-show staging combines broadcast XR, camera effects, large LED backdrops, and fast-changing performance sets.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/MAMA_Awards_logo.svg/640px-MAMA_Awards_logo.svg.png",
        "visual_link": "https://www.youtube.com/results?search_query=MAMA+Awards+XR+stage+performance"
    },
    {
        "artist": "Coachella",
        "title": "K-pop Festival Stages",
        "logo": "COACHELLA",
        "venue": "Coachella Stage",
        "scale": "Outdoor Festival",
        "audience": "Large Festival",
        "year": "2019–2024",
        "production": "Festival Production",
        "tags": ["LED Wall", "Laser System", "Projection Mapping"],
        "analysis": "Outdoor festival staging emphasizes strong screen visibility, simplified scenic structure, and broadcast impact.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Coachella_2018_%2840489809670%29.jpg/640px-Coachella_2018_%2840489809670%29.jpg",
        "visual_link": "https://www.youtube.com/results?search_query=Kpop+Coachella+stage+performance"
    }
]

all_tags = sorted(set(tag for concert in concerts for tag in concert["tags"]))


def safe_image(url, fallback_text):
    try:
        st.image(url, width="stretch")
    except Exception:
        st.markdown(
            f'<div class="logo-fallback">{fallback_text}</div>',
            unsafe_allow_html=True
        )


def tag_html(tags):
    return "".join([f'<span class="tech-pill">{tag}</span>' for tag in tags])


def render_card(concert):
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        safe_image(concert["image"], concert["logo"])
        st.subheader(concert["title"])
        st.markdown(
            f"""
            <p class="meta-text">
            <b>Artist / Event</b> — {concert['artist']}<br>
            <b>Venue</b> — {concert['venue']}<br>
            <b>Scale</b> — {concert['scale']}<br>
            <b>Audience</b> — {concert['audience']}<br>
            <b>Year</b> — {concert['year']}<br>
            <b>Production</b> — {concert['production']}
            </p>
            """,
            unsafe_allow_html=True
        )
        st.markdown(f'<p class="analysis-text">{concert["analysis"]}</p>', unsafe_allow_html=True)
        st.markdown(tag_html(concert["tags"]), unsafe_allow_html=True)
        st.link_button("Open Visual Reference", concert["visual_link"])
        st.markdown('</div>', unsafe_allow_html=True)


st.markdown(
    """
    <div class="hero-box">
        <div style="font-size:16px; font-weight:800; color:#ffb4ea !important;">
        K-pop Concert Technology Visual Archive
        </div>
        <div class="hero-title">
        Stage<span class="glow-text">Scape</span>
        </div>
        <div class="hero-subtitle">
        Explore K-pop concert production through stage technology, venue scale,
        visual direction, image references, and performance design systems.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs([
    "Technology → Concert Analysis",
    "Concert → Technology Analysis",
    "Visual Reference Gallery"
])

with tab1:
    st.header("Explore by Stage Technology")

    selected_tag = st.selectbox("Select Technology", ["All"] + all_tags)

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

    selected_title = st.selectbox(
        "Select Concert",
        [concert["title"] for concert in concerts],
        key="concert_select"
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
            if related:
                st.write("Related concerts:")
                for title in related[:8]:
                    st.write(f"• {title}")
            else:
                st.write("No related concerts in the current archive.")

with tab3:
    st.header("Visual Reference Gallery")
    st.write(
        "This section shows visual thumbnails inside the page and also provides links to actual performance footage."
    )

    selected_visual_tag = st.selectbox(
        "Filter Gallery by Technology",
        ["All"] + all_tags,
        key="visual_select"
    )

    if selected_visual_tag == "All":
        gallery = concerts
    else:
        gallery = [concert for concert in concerts if selected_visual_tag in concert["tags"]]

    cols = st.columns(3)
    for idx, concert in enumerate(gallery):
        with cols[idx % 3]:
            with st.container(border=True):
                safe_image(concert["image"], concert["logo"])
                st.subheader(concert["artist"])
                st.write(concert["title"])
                st.markdown(tag_html(concert["tags"]), unsafe_allow_html=True)
                st.link_button("Watch / Search Stage", concert["visual_link"])

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

with s1:
    st.markdown(f'<div class="stat-box"><div class="stat-number">{len(concerts)}</div><div class="stat-label">Concert Cases</div></div>', unsafe_allow_html=True)

with s2:
    st.markdown(f'<div class="stat-box"><div class="stat-number">{len(all_tags)}</div><div class="stat-label">Technology Tags</div></div>', unsafe_allow_html=True)

with s3:
    st.markdown(f'<div class="stat-box"><div class="stat-number">{len(set(c["artist"] for c in concerts))}</div><div class="stat-label">Artists & Events</div></div>', unsafe_allow_html=True)

with s4:
    st.markdown(f'<div class="stat-box"><div class="stat-number">{len(set(c["scale"] for c in concerts))}</div><div class="stat-label">Venue Types</div></div>', unsafe_allow_html=True)

st.divider()
st.caption("StageScape — K-pop Concert Stage Technology Visual Archive")
