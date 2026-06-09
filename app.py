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
    radial-gradient(circle at 10% 5%, rgba(255, 0, 150, 0.32), transparent 28%),
    radial-gradient(circle at 90% 10%, rgba(0, 200, 255, 0.25), transparent 30%),
    radial-gradient(circle at 50% 100%, rgba(140, 80, 255, 0.28), transparent 35%),
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

.stSelectbox label {
    color: white !important;
    font-weight: 800 !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #111111 !important;
}

.stSelectbox div[data-baseweb="select"] span {
    color: #111111 !important;
}

div[data-baseweb="popover"] {
    background-color: #ffffff !important;
}

div[data-baseweb="popover"] * {
    color: #111111 !important;
}

button[data-baseweb="tab"] p {
    color: #ffffff !important;
    font-weight: 700 !important;
}

button[data-baseweb="tab"][aria-selected="true"] p {
    color: #ff5ac8 !important;
}

.hero-box {
    padding: 56px;
    border-radius: 36px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.22);
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

.glow-text {
    background: linear-gradient(90deg, #ffffff, #ff6bd6, #62d8ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 22px;
    color: #e8e8e8 !important;
    line-height: 1.7;
    margin-top: 22px;
}

.card {
    background: rgba(8,8,16,0.88);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 30px;
    padding: 26px;
    margin-bottom: 30px;
    box-shadow: 0 24px 60px rgba(0,0,0,0.38);
}

.visual-card {
    height: 230px;
    border-radius: 28px;
    background:
    linear-gradient(135deg, rgba(255,60,180,0.9), rgba(55,145,255,0.85)),
    radial-gradient(circle at top left, rgba(255,255,255,0.35), transparent 35%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 34px;
    margin-bottom: 24px;
    border: 1px solid rgba(255,255,255,0.25);
    overflow: hidden;
}

.visual-logo {
    font-size: 40px;
    font-weight: 950;
    letter-spacing: -1px;
    color: white !important;
}

.visual-sub {
    margin-top: 10px;
    font-size: 15px;
    color: rgba(255,255,255,0.88) !important;
}

.meta-text {
    color: #eeeeee !important;
    line-height: 1.75;
    font-size: 16px;
}

.analysis-text {
    color: #dddddd !important;
    line-height: 1.85;
    font-size: 16px;
}

.tech-pill {
    display: inline-block;
    background: linear-gradient(135deg, #ff3cac, #784ba0, #2b86c5);
    color: white !important;
    padding: 9px 15px;
    border-radius: 999px;
    margin-right: 8px;
    margin-bottom: 8px;
    font-size: 12px;
    font-weight: 800;
}

.reference-button {
    display: inline-block;
    margin-top: 18px;
    padding: 12px 18px;
    border-radius: 14px;
    background: #ffffff;
    color: #111111 !important;
    font-weight: 800;
    text-decoration: none !important;
}

.reference-button:hover {
    background: #ff5ac8;
    color: white !important;
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

/* ===== SELECTBOX TEXT FIX ===== */

/* 선택박스 본문 */
div[data-baseweb="select"] {
    background: white !important;
}

/* 선택된 값 */
div[data-baseweb="select"] span {
    color: black !important;
}

/* 입력 텍스트 */
div[data-baseweb="select"] input {
    color: black !important;
    -webkit-text-fill-color: black !important;
}

/* 드롭다운 목록 */
div[role="listbox"] {
    background: white !important;
}

/* 드롭다운 항목 */
div[role="option"] {
    color: black !important;
}

/* 선택된 항목 */
div[aria-selected="true"] {
    color: black !important;
}

/* 화살표 */
div[data-baseweb="select"] svg {
    fill: black !important;
}
</style>
""", unsafe_allow_html=True)


concerts = [
    {"artist":"BTS","title":"Permission To Dance On Stage","logo":"BTS","venue":"SoFi Stadium / Olympic Stadium","scale":"Mega Stadium","audience":"50,000+","year":"2021–2022","production":"HYBE Production","tags":["LED Wall","Projection Mapping","Automated Lift","Moving Runway"],"analysis":"Stadium-scale LED screens and extended runways were used to keep the performance visible and immersive across a very large venue.","visual_link":"https://www.youtube.com/results?search_query=BTS+Permission+To+Dance+On+Stage+concert"},
    {"artist":"BTS","title":"Love Yourself: Speak Yourself","logo":"BTS","venue":"Wembley Stadium / Global Stadiums","scale":"World Stadium Tour","audience":"60,000+","year":"2019","production":"Big Hit Production","tags":["LED Wall","Pyrotechnics","Moving Runway","Laser System"],"analysis":"A stadium-scale tour using large LED architecture, fireworks, and extended stage routes to connect with distant audience sections.","visual_link":"https://www.youtube.com/results?search_query=BTS+Speak+Yourself+Wembley+stage"},
    {"artist":"BLACKPINK","title":"BORN PINK WORLD TOUR","logo":"BLACKPINK","venue":"Gocheok Sky Dome / Global Stadiums","scale":"World Stadium Tour","audience":"55,000+","year":"2022–2023","production":"YG Stage Team","tags":["LED Wall","Kinetic Stage","Laser System","Drone Show"],"analysis":"The tour used bold LED visuals, strong lighting contrast, and moving stage structures to create a luxury-pop concert identity.","visual_link":"https://www.youtube.com/results?search_query=BLACKPINK+BORN+PINK+WORLD+TOUR+stage"},
    {"artist":"BLACKPINK","title":"IN YOUR AREA WORLD TOUR","logo":"BLACKPINK","venue":"Global Arenas","scale":"World Arena Tour","audience":"10,000–20,000","year":"2018–2020","production":"YG Entertainment","tags":["LED Wall","Laser System","Moving Runway"],"analysis":"Arena-scale screens and runways supported the group’s strong performance identity and direct audience interaction.","visual_link":"https://www.youtube.com/results?search_query=BLACKPINK+IN+YOUR+AREA+concert+stage"},
    {"artist":"BIGBANG","title":"MADE WORLD TOUR","logo":"BIGBANG","venue":"Olympic Gymnastics Arena / Global Arenas","scale":"World Tour","audience":"Large Arena","year":"2015–2016","production":"YG Entertainment","tags":["LED Wall","Kinetic Stage","Laser System"],"analysis":"A bold arena concert structure built around large video screens, band-like performance energy, and dramatic light transitions.","visual_link":"https://www.youtube.com/results?search_query=BIGBANG+MADE+Tour+stage"},
    {"artist":"G-DRAGON","title":"ACT III: M.O.T.T.E","logo":"G-DRAGON","venue":"World Tour Arenas","scale":"Solo World Tour","audience":"Large Arena","year":"2017","production":"YG Entertainment","tags":["LED Wall","Projection Mapping","Laser System"],"analysis":"A highly art-directed solo concert using symbolic visuals, intense red lighting, and theatrical screen imagery.","visual_link":"https://www.youtube.com/results?search_query=G-DRAGON+MOTTE+concert+stage"},
    {"artist":"aespa","title":"SYNK: HYPER LINE","logo":"aespa","venue":"KSPO Dome","scale":"Arena Tour","audience":"15,000+","year":"2023","production":"SM Visual Production","tags":["XR","AR Camera","LED Wall","Virtual Production"],"analysis":"The concert connects aespa’s virtual-world concept with avatar-like visuals, immersive LED environments, and camera-based digital effects.","visual_link":"https://www.youtube.com/results?search_query=aespa+SYNK+HYPER+LINE+concert+stage"},
    {"artist":"aespa","title":"SYNK: PARALLEL LINE","logo":"aespa","venue":"Jamsil Indoor Stadium / Global Arenas","scale":"Arena Tour","audience":"10,000+","year":"2024","production":"SM Visual Production","tags":["XR","LED Wall","AR Camera","Laser System"],"analysis":"A performance system continuing aespa’s digital-world identity through layered LED space, cyber visuals, and camera-based effects.","visual_link":"https://www.youtube.com/results?search_query=aespa+SYNK+PARALLEL+LINE+concert+stage"},
    {"artist":"NCT 127","title":"NEO CITY: THE LINK","logo":"NCT 127","venue":"Tokyo Dome / KSPO Dome","scale":"Dome Tour","audience":"50,000+","year":"2022–2023","production":"SM Stage Division","tags":["XR","Kinetic Stage","LED Wall","Laser System"],"analysis":"Cyberpunk-inspired visuals, modular stage construction, and intense lighting systems created a futuristic concert identity.","visual_link":"https://www.youtube.com/results?search_query=NCT+127+NEO+CITY+THE+LINK+concert+stage"},
    {"artist":"NCT DREAM","title":"THE DREAM SHOW 2","logo":"NCT DREAM","venue":"Jamsil Olympic Stadium / Global Arenas","scale":"Stadium / Arena Tour","audience":"30,000+","year":"2022–2023","production":"SM Entertainment","tags":["LED Wall","Moving Runway","Confetti System","Laser System"],"analysis":"Large LED screens and extended stage routes support youthful energy and high audience contact across a large venue.","visual_link":"https://www.youtube.com/results?search_query=NCT+DREAM+THE+DREAM+SHOW+2+stage"},
    {"artist":"NCT DREAM","title":"THE DREAM SHOW 3","logo":"NCT DREAM","venue":"Gocheok Sky Dome / Global Arenas","scale":"Dome / Arena Tour","audience":"20,000+","year":"2024","production":"SM Entertainment","tags":["LED Wall","Kinetic Stage","Laser System"],"analysis":"A dome-scale visual system built around bright LED graphics, large stage depth, and synchronized light movement.","visual_link":"https://www.youtube.com/results?search_query=NCT+DREAM+THE+DREAM+SHOW+3+stage"},
    {"artist":"NCT WISH","title":"NCT WISH ASIA TOUR","logo":"NCT WISH","venue":"Asia Tour Venues","scale":"Theater / Arena Tour","audience":"Small–Mid Venue","year":"2024–2025","production":"SM Entertainment","tags":["LED Wall","Projection Mapping","Interactive LED"],"analysis":"A smaller-scale tour format using clean LED graphics and character-driven visual elements to build group identity.","visual_link":"https://www.youtube.com/results?search_query=NCT+WISH+concert+stage"},
    {"artist":"EXO","title":"EXO PLANET #2: The EXO'luxion","logo":"EXO","venue":"Olympic Gymnastics Arena / Global Arenas","scale":"Arena Tour","audience":"15,000+","year":"2015–2016","production":"SM Entertainment","tags":["Hologram","LED Wall","Projection Mapping","Moving Runway"],"analysis":"Earlier large-scale K-pop touring used hologram-like effects, theatrical VCRs, and fantasy stage environments.","visual_link":"https://www.youtube.com/results?search_query=EXO+PLANET+EXOluxion+hologram+stage"},
    {"artist":"EXO","title":"EXO PLANET #5: EXplOration","logo":"EXO","venue":"KSPO Dome / Global Arenas","scale":"Arena Tour","audience":"15,000+","year":"2019","production":"SM Entertainment","tags":["LED Wall","Laser System","Projection Mapping"],"analysis":"A polished arena-stage system using sci-fi visuals, strong LED backdrops, and dramatic performance lighting.","visual_link":"https://www.youtube.com/results?search_query=EXO+EXplOration+concert+stage"},
    {"artist":"SHINee","title":"SHINee WORLD VI: PERFECT ILLUMINATION","logo":"SHINee","venue":"KSPO Dome / Tokyo Dome","scale":"Arena / Dome Tour","audience":"15,000–50,000","year":"2023–2024","production":"SM Entertainment","tags":["LED Wall","Laser System","Moving Runway","Follow Spot System"],"analysis":"Lighting design plays a central role, supporting SHINee’s performance identity with precise spotlights and elegant screen visuals.","visual_link":"https://www.youtube.com/results?search_query=SHINee+PERFECT+ILLUMINATION+concert+stage"},
    {"artist":"TVXQ","title":"TVXQ LIVE TOUR","logo":"TVXQ","venue":"Tokyo Dome / Nissan Stadium","scale":"Dome / Stadium Tour","audience":"50,000+","year":"2013–2019","production":"SM / Avex","tags":["LED Wall","Moving Runway","Pyrotechnics","Automated Lift"],"analysis":"Large Japanese dome and stadium productions rely on massive runways, lifts, and pyrotechnics to sustain scale and visibility.","visual_link":"https://www.youtube.com/results?search_query=TVXQ+Tokyo+Dome+concert+stage"},
    {"artist":"Red Velvet","title":"R to V","logo":"Red Velvet","venue":"KSPO Dome / Global Venues","scale":"Arena Tour","audience":"10,000+","year":"2023","production":"SM Entertainment","tags":["LED Wall","Projection Mapping","Theatrical Set"],"analysis":"A concept-driven show using contrasting visual worlds, scenic set changes, and screen graphics to reflect dual identities.","visual_link":"https://www.youtube.com/results?search_query=Red+Velvet+R+to+V+concert+stage"},
    {"artist":"SEVENTEEN","title":"FOLLOW TOUR","logo":"SEVENTEEN","venue":"Seoul / Tokyo Dome","scale":"Dome Tour","audience":"45,000+","year":"2023–2024","production":"PLEDIS Production","tags":["LED Wall","Kinetic Stage","Automated Lift","Moving Runway"],"analysis":"Extended stage architecture and moving platforms support group choreography while increasing audience connection in large dome venues.","visual_link":"https://www.youtube.com/results?search_query=SEVENTEEN+FOLLOW+TOUR+stage"},
    {"artist":"SEVENTEEN","title":"BE THE SUN","logo":"SEVENTEEN","venue":"Gocheok Sky Dome / Global Arenas","scale":"World Arena Tour","audience":"20,000+","year":"2022","production":"PLEDIS Production","tags":["LED Wall","Laser System","Moving Runway"],"analysis":"A bright and powerful concert design using large LED screens and runways to support high-energy group choreography.","visual_link":"https://www.youtube.com/results?search_query=SEVENTEEN+BE+THE+SUN+concert+stage"},
    {"artist":"TXT","title":"ACT: SWEET MIRAGE","logo":"TXT","venue":"KSPO Dome / Global Arenas","scale":"Arena Tour","audience":"15,000+","year":"2023","production":"HYBE Production","tags":["Projection Mapping","LED Wall","Automated Lift","Theatrical Set"],"analysis":"Fantasy-like visual direction is supported through scenic LED imagery, theatrical transitions, and layered stage space.","visual_link":"https://www.youtube.com/results?search_query=TXT+ACT+SWEET+MIRAGE+stage"},
    {"artist":"TXT","title":"ACT: PROMISE","logo":"TXT","venue":"KSPO Dome / Global Arenas","scale":"Arena Tour","audience":"15,000+","year":"2024","production":"HYBE Production","tags":["LED Wall","Projection Mapping","Moving Runway"],"analysis":"A narrative-driven arena show using wide LED compositions and scenic transitions to connect performances into a fantasy journey.","visual_link":"https://www.youtube.com/results?search_query=TXT+ACT+PROMISE+concert+stage"},
    {"artist":"ENHYPEN","title":"FATE Tour","logo":"ENHYPEN","venue":"KSPO Dome / Global Arenas","scale":"Arena Tour","audience":"15,000+","year":"2023–2024","production":"BELIFT / HYBE","tags":["LED Wall","Projection Mapping","Kinetic Stage","Laser System"],"analysis":"Dark fantasy visuals and moving stage structures build a dramatic narrative-oriented concert atmosphere.","visual_link":"https://www.youtube.com/results?search_query=ENHYPEN+FATE+Tour+stage"},
    {"artist":"ENHYPEN","title":"MANIFESTO Tour","logo":"ENHYPEN","venue":"Global Arenas","scale":"Arena Tour","audience":"10,000+","year":"2022–2023","production":"BELIFT / HYBE","tags":["LED Wall","Laser System","Moving Runway"],"analysis":"High-contrast lighting and large video walls reinforce the group’s dark performance style and narrative imagery.","visual_link":"https://www.youtube.com/results?search_query=ENHYPEN+MANIFESTO+concert+stage"},
    {"artist":"LE SSERAFIM","title":"FLAME RISES","logo":"LE SSERAFIM","venue":"Jamsil Indoor Stadium","scale":"Arena Concert","audience":"10,000+","year":"2023","production":"Source Music / HYBE","tags":["LED Wall","Laser System","Automated Lift"],"analysis":"Minimal but powerful stage visuals emphasize choreography, confidence, and strong lighting contrast.","visual_link":"https://www.youtube.com/results?search_query=LE+SSERAFIM+FLAME+RISES+concert+stage"},
    {"artist":"NewJeans","title":"Lollapalooza / Bunnies Camp","logo":"NewJeans","venue":"Festival Stage / Fan Meeting Venue","scale":"Festival / Fan Meeting","audience":"Large Festival","year":"2023–2024","production":"ADOR","tags":["LED Wall","Projection Mapping","Graphic Screen Design"],"analysis":"Clean graphic visuals and retro-inspired screen design support the group’s casual and nostalgic visual identity.","visual_link":"https://www.youtube.com/results?search_query=NewJeans+Lollapalooza+stage"},
    {"artist":"TWS","title":"Fan Meeting / Showcase Stages","logo":"TWS","venue":"Showcase Venues","scale":"Showcase / Fan Meeting","audience":"Small–Mid Venue","year":"2024","production":"PLEDIS Production","tags":["LED Wall","Graphic Screen Design","Follow Spot System"],"analysis":"A clean debut-stage system using bright LED graphics and simple spatial composition to highlight group identity.","visual_link":"https://www.youtube.com/results?search_query=TWS+showcase+stage"},
    {"artist":"BOYNEXTDOOR","title":"ONEDOORful Day","logo":"BND","venue":"Fan Meeting Venues","scale":"Fan Meeting / Theater","audience":"Small–Mid Venue","year":"2024","production":"KOZ / HYBE","tags":["LED Wall","Theatrical Set","Graphic Screen Design"],"analysis":"Set-based staging and approachable graphics create a neighborhood-themed performance atmosphere.","visual_link":"https://www.youtube.com/results?search_query=BOYNEXTDOOR+concert+stage"},
    {"artist":"Stray Kids","title":"MANIAC / 5-STAR Tour","logo":"SKZ","venue":"KSPO Dome / Global Arenas","scale":"Arena Tour","audience":"15,000–40,000","year":"2022–2024","production":"JYP Production","tags":["LED Wall","Laser System","Kinetic Stage","Pyrotechnics"],"analysis":"Sharp lighting, industrial video design, and powerful LED environments match the group’s intense performance style.","visual_link":"https://www.youtube.com/results?search_query=Stray+Kids+MANIAC+concert+stage"},
    {"artist":"Stray Kids","title":"dominATE World Tour","logo":"SKZ","venue":"Global Stadiums / Arenas","scale":"World Tour","audience":"Large Arena / Stadium","year":"2024–2025","production":"JYP Production","tags":["LED Wall","Laser System","Moving Runway","Pyrotechnics"],"analysis":"A larger tour format emphasizing aggressive lighting, stadium visibility, and high-impact performance moments.","visual_link":"https://www.youtube.com/results?search_query=Stray+Kids+dominATE+world+tour+stage"},
    {"artist":"TWICE","title":"READY TO BE","logo":"TWICE","venue":"KSPO Dome / Global Stadiums","scale":"World Stadium Tour","audience":"40,000+","year":"2023–2024","production":"JYP Production","tags":["LED Wall","Kinetic Stage","Automated Lift","Moving Runway"],"analysis":"A bright pop concert system designed for member movement, large audience visibility, and colorful screen-based production.","visual_link":"https://www.youtube.com/results?search_query=TWICE+READY+TO+BE+concert+stage"},
    {"artist":"TWICE","title":"III World Tour","logo":"TWICE","venue":"KSPO Dome / Global Arenas","scale":"World Arena Tour","audience":"10,000–20,000","year":"2021–2022","production":"JYP Production","tags":["LED Wall","Moving Runway","Confetti System"],"analysis":"A flexible arena setup combining vivid screens, extended stages, and celebratory audience effects.","visual_link":"https://www.youtube.com/results?search_query=TWICE+III+World+Tour+stage"},
    {"artist":"ITZY","title":"CHECKMATE Tour","logo":"ITZY","venue":"Global Arenas","scale":"World Tour","audience":"10,000+","year":"2022–2023","production":"JYP Production","tags":["LED Wall","Laser System","Moving Runway"],"analysis":"High-energy lighting and LED visuals support sharp choreography and confident performance branding.","visual_link":"https://www.youtube.com/results?search_query=ITZY+CHECKMATE+concert+stage"},
    {"artist":"ITZY","title":"BORN TO BE Tour","logo":"ITZY","venue":"Jamsil Indoor Stadium / Global Venues","scale":"World Tour","audience":"10,000+","year":"2024","production":"JYP Production","tags":["LED Wall","Laser System","Automated Lift"],"analysis":"A more intense stage identity built through dark lighting, powerful screen graphics, and choreographic focus.","visual_link":"https://www.youtube.com/results?search_query=ITZY+BORN+TO+BE+concert+stage"},
    {"artist":"NMIXX","title":"NICE TO MIXX YOU","logo":"NMIXX","venue":"Theater / Arena Venues","scale":"Showcase Tour","audience":"Small–Mid Venue","year":"2023","production":"JYP Production","tags":["LED Wall","Graphic Screen Design","Follow Spot System"],"analysis":"Compact tour staging uses graphic LED visuals and clean lighting to support live vocals and performance transitions.","visual_link":"https://www.youtube.com/results?search_query=NMIXX+NICE+TO+MIXX+YOU+stage"},
    {"artist":"IVE","title":"SHOW WHAT I HAVE","logo":"IVE","venue":"KSPO Dome / Global Arenas","scale":"Arena Tour","audience":"15,000+","year":"2023–2024","production":"Starship Entertainment","tags":["LED Wall","Automated Lift","Projection Mapping"],"analysis":"Elegant large-screen visuals and vertical stage composition reinforce the group’s polished performance image.","visual_link":"https://www.youtube.com/results?search_query=IVE+SHOW+WHAT+I+HAVE+concert+stage"},
    {"artist":"MONSTA X","title":"NO LIMIT Tour","logo":"MONSTA X","venue":"Global Arenas","scale":"World Tour","audience":"Large Arena","year":"2022","production":"Starship Entertainment","tags":["LED Wall","Laser System","Pyrotechnics"],"analysis":"Strong lighting, large screens, and explosive effects support a powerful performance-centered concert image.","visual_link":"https://www.youtube.com/results?search_query=MONSTA+X+NO+LIMIT+concert+stage"},
    {"artist":"IU","title":"The Golden Hour","logo":"IU","venue":"Olympic Stadium","scale":"Stadium Concert","audience":"45,000+ per day","year":"2022","production":"EDAM Production","tags":["Drone Show","Projection Mapping","LED Wall","Follow Spot System"],"analysis":"Drone visuals, warm lighting, and poetic stadium-scale screen design created an emotional visual narrative.","visual_link":"https://www.youtube.com/results?search_query=IU+The+Golden+Hour+concert+drone+show"},
    {"artist":"IU","title":"HEREH World Tour","logo":"IU","venue":"KSPO Dome / Global Arenas","scale":"World Tour","audience":"10,000+","year":"2024","production":"EDAM Production","tags":["LED Wall","Projection Mapping","Moving Runway"],"analysis":"A refined world-tour system using emotional screen imagery, delicate lighting, and strong audience intimacy.","visual_link":"https://www.youtube.com/results?search_query=IU+HEREH+World+Tour+stage"},
    {"artist":"TAEMIN","title":"METAMORPH","logo":"TAEMIN","venue":"Inspire Arena","scale":"Arena Concert","audience":"10,000+","year":"2023","production":"SM Entertainment","tags":["Kinetic Stage","LED Wall","Laser System","Theatrical Set"],"analysis":"A performance-art-oriented concert using dramatic structures, controlled lighting, and choreographic staging.","visual_link":"https://www.youtube.com/results?search_query=TAEMIN+METAMORPH+concert+stage"},
    {"artist":"TAEYEON","title":"The ODD Of LOVE","logo":"TAEYEON","venue":"KSPO Dome / Asia Venues","scale":"Arena Tour","audience":"10,000+","year":"2023","production":"SM Entertainment","tags":["LED Wall","Projection Mapping","Follow Spot System"],"analysis":"A vocal-centered concert where lighting and screen imagery create mood shifts without overpowering the performer.","visual_link":"https://www.youtube.com/results?search_query=TAEYEON+The+ODD+Of+LOVE+concert+stage"},
    {"artist":"MAMA Awards","title":"MAMA Awards Stage","logo":"MAMA","venue":"Kyocera Dome / Tokyo Dome","scale":"Award Ceremony","audience":"40,000+","year":"2023–2024","production":"CJ ENM","tags":["XR","Projection Mapping","AR Camera","LED Wall","Virtual Production"],"analysis":"Award-show staging combines broadcast XR, camera effects, large LED backdrops, and fast-changing performance sets.","visual_link":"https://www.youtube.com/results?search_query=MAMA+Awards+XR+stage+performance"},
    {"artist":"Melon Music Awards","title":"MMA Stage","logo":"MMA","venue":"Inspire Arena / Gocheok Sky Dome","scale":"Award Ceremony","audience":"Large Arena","year":"2022–2024","production":"Kakao / Melon","tags":["LED Wall","Projection Mapping","AR Camera"],"analysis":"Broadcast-focused stage design uses large LED systems and camera effects to highlight individual artist concepts.","visual_link":"https://www.youtube.com/results?search_query=Melon+Music+Awards+stage+performance"},
    {"artist":"Golden Disc Awards","title":"Golden Disc Awards Stage","logo":"GDA","venue":"Global Arena Venues","scale":"Award Ceremony","audience":"Large Arena","year":"2022–2024","production":"GDA Production","tags":["LED Wall","Laser System","Projection Mapping"],"analysis":"Award-show staging uses flexible LED backdrops and fast transition systems for multiple artists in one event.","visual_link":"https://www.youtube.com/results?search_query=Golden+Disc+Awards+Kpop+stage"},
    {"artist":"SBS Gayo Daejeon","title":"SBS Gayo Daejeon Stage","logo":"SBS GAYO","venue":"Inspire Arena / Gocheok Sky Dome","scale":"Broadcast Festival","audience":"Large Arena","year":"2022–2024","production":"SBS","tags":["LED Wall","AR Camera","Projection Mapping","Laser System"],"analysis":"Broadcast-oriented production combines large LED screens, camera movement, and quick scenic changes between teams.","visual_link":"https://www.youtube.com/results?search_query=SBS+Gayo+Daejeon+stage+performance"},
    {"artist":"KBS Song Festival","title":"KBS Gayo Stage","logo":"KBS GAYO","venue":"Broadcast / Arena Venues","scale":"Broadcast Festival","audience":"Broadcast Audience","year":"2022–2024","production":"KBS","tags":["LED Wall","AR Camera","Moving Runway"],"analysis":"A multi-artist broadcast stage using camera-led composition, LED graphics, and modular stage layouts.","visual_link":"https://www.youtube.com/results?search_query=KBS+Song+Festival+Kpop+stage"},
    {"artist":"MBC Gayo Daejejeon","title":"MBC Gayo Stage","logo":"MBC GAYO","venue":"Broadcast / Arena Venues","scale":"Broadcast Festival","audience":"Broadcast Audience","year":"2022–2024","production":"MBC","tags":["LED Wall","Projection Mapping","AR Camera"],"analysis":"Year-end broadcast production uses symbolic set pieces and digital effects to build event-scale visual identity.","visual_link":"https://www.youtube.com/results?search_query=MBC+Gayo+Daejejeon+Kpop+stage"},
    {"artist":"SMTOWN","title":"SMTOWN LIVE","logo":"SMTOWN","venue":"Suwon World Cup Stadium / Tokyo Dome","scale":"Family Concert / Stadium","audience":"40,000+","year":"2022–2024","production":"SM Entertainment","tags":["LED Wall","Moving Runway","Laser System","Pyrotechnics"],"analysis":"A large label-family concert format requiring flexible stage systems for many artists and quick performance transitions.","visual_link":"https://www.youtube.com/results?search_query=SMTOWN+LIVE+concert+stage"},
    {"artist":"KCON","title":"KCON Stage","logo":"KCON","venue":"LA / Japan / Global Arenas","scale":"Convention Concert","audience":"Large Arena","year":"2022–2024","production":"CJ ENM","tags":["LED Wall","AR Camera","Projection Mapping","Graphic Screen Design"],"analysis":"Convention concert staging uses modular production and strong screen branding to support many artists in one program.","visual_link":"https://www.youtube.com/results?search_query=KCON+concert+stage+performance"},
    {"artist":"Dream Concert","title":"Dream Concert Stage","logo":"DREAM CONCERT","venue":"Seoul World Cup Stadium / Large Venues","scale":"Multi-Artist Stadium Event","audience":"40,000+","year":"2015–2024","production":"Korea Entertainment Producers Association","tags":["LED Wall","Moving Runway","Pyrotechnics","Follow Spot System"],"analysis":"A mass multi-artist event format built around visibility, fast turnovers, and large stadium audience communication.","visual_link":"https://www.youtube.com/results?search_query=Dream+Concert+Kpop+stage"},
    {"artist":"Coachella","title":"K-pop Festival Stages","logo":"COACHELLA","venue":"Coachella Stage","scale":"Outdoor Festival","audience":"Large Festival","year":"2019–2024","production":"Festival Production","tags":["LED Wall","Laser System","Projection Mapping","Pyrotechnics"],"analysis":"Outdoor festival staging emphasizes strong screen visibility, simplified scenic structure, and broadcast impact.","visual_link":"https://www.youtube.com/results?search_query=Kpop+Coachella+stage+performance"},
    {"artist":"Lollapalooza","title":"K-pop Festival Performances","logo":"LOLLA","venue":"Grant Park / Festival Stage","scale":"Outdoor Festival","audience":"Large Festival","year":"2022–2024","production":"Festival Production","tags":["LED Wall","Laser System","Graphic Screen Design"],"analysis":"Festival stages rely on wide LED visibility and strong visual branding that can communicate quickly to mixed audiences.","visual_link":"https://www.youtube.com/results?search_query=Kpop+Lollapalooza+stage+performance"},
    {"artist":"Summer Sonic","title":"K-pop Festival Stages","logo":"SUMMER SONIC","venue":"Japan Festival Stages","scale":"Outdoor / Indoor Festival","audience":"Large Festival","year":"2022–2024","production":"Festival Production","tags":["LED Wall","Laser System","Follow Spot System"],"analysis":"Festival staging focuses on flexible lighting, clean screen visuals, and fast setup for multiple artist lineups.","visual_link":"https://www.youtube.com/results?search_query=Kpop+Summer+Sonic+stage"},
]

all_tags = sorted(set(tag for concert in concerts for tag in concert["tags"]))


def tag_html(tags):
    return "".join([f'<span class="tech-pill">{tag}</span>' for tag in tags])


def visual_card(concert):
    st.markdown(
        f"""
        <div class="visual-card">
            <div class="visual-logo">{concert["logo"]}</div>
            <div class="visual-sub">{concert["title"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def reference_button(concert):
    st.markdown(
        f"""
        <a class="reference-button" href="{concert["visual_link"]}" target="_blank">
            Open Visual Reference
        </a>
        """,
        unsafe_allow_html=True
    )


def render_card(concert):
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        visual_card(concert)
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
        reference_button(concert)
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
        visual direction, visual reference cards, and performance design systems.
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
                for title in related[:10]:
                    st.write(f"• {title}")
            else:
                st.write("No related concerts in the current archive.")

with tab3:
    st.header("Visual Reference Gallery")
    st.write(
        "This section avoids unstable image loading by using generated visual cards. "
        "Each card links to actual performance footage and stage references."
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
                visual_card(concert)
                st.subheader(concert["artist"])
                st.write(concert["title"])
                st.markdown(tag_html(concert["tags"]), unsafe_allow_html=True)
                reference_button(concert)

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
