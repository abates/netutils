"""Constant definitions used in project."""
from netutils.data_files.protocol_mappings import PROTOCOLS  # noqa: F401 # pylint:disable=unused-import


# This variable provides mapping for known interface variants, to the associated long form.
BASE_INTERFACES = {
    "Ap": "AppGigabitEthernet",
    "ap": "AppGigabitEthernet",
    "ATM": "ATM",
    "AT": "ATM",
    "B": "Bdi",
    "Bd": "Bdi",
    "Bdi": "Bdi",
    "Bridge-Aggregation": "Port-channel",
    "EOBC": "EOBC",
    "EO": "EOBC",
    "Ethernet": "Ethernet",
    "Eth": "Ethernet",
    "eth": "Ethernet",
    "Et": "Ethernet",
    "et": "Ethernet",
    "FastEthernet": "FastEthernet",
    "FastEth": "FastEthernet",
    "FastE": "FastEthernet",
    "Fast": "FastEthernet",
    "Fas": "FastEthernet",
    "FE": "FastEthernet",
    "Fa": "FastEthernet",
    "fa": "FastEthernet",
    "Fddi": "Fddi",
    "FD": "Fddi",
    "FortyGigabitEthernet": "FortyGigabitEthernet",
    "FortyGigEthernet": "FortyGigabitEthernet",
    "FortyGigEth": "FortyGigabitEthernet",
    "FortyGigE": "FortyGigabitEthernet",
    "FortyGig": "FortyGigabitEthernet",
    "FGE": "FortyGigabitEthernet",
    "FO": "FortyGigabitEthernet",
    "Fo": "FortyGigabitEthernet",
    "FiftyGigabitEthernet": "FiftyGigabitEthernet",
    "FiftyGigEthernet": "FiftyGigabitEthernet",
    "FiftyGigEth": "FiftyGigabitEthernet",
    "FiftyGigE": "FiftyGigabitEthernet",
    "FI": "FiftyGigabitEthernet",
    "Fi": "FiftyGigabitEthernet",
    "fi": "FiftyGigabitEthernet",
    "GigabitEthernet": "GigabitEthernet",
    "GigEthernet": "GigabitEthernet",
    "GigEth": "GigabitEthernet",
    "GigE": "GigabitEthernet",
    "Gig": "GigabitEthernet",
    "GE": "GigabitEthernet",
    "Ge": "GigabitEthernet",
    "ge": "GigabitEthernet",
    "Gi": "GigabitEthernet",
    "gi": "GigabitEthernet",
    "HundredGigabitEthernet": "HundredGigabitEthernet",
    "HundredGigEthernet": "HundredGigabitEthernet",
    "HundredGigEth": "HundredGigabitEthernet",
    "HundredGigE": "HundredGigabitEthernet",
    "HundredGig": "HundredGigabitEthernet",
    "Hu": "HundredGigabitEthernet",
    "TwentyFiveGigabitEthernet": "TwentyFiveGigE",
    "TwentyFiveGigEthernet": "TwentyFiveGigE",
    "TwentyFiveGigEth": "TwentyFiveGigE",
    "TwentyFiveGigE": "TwentyFiveGigE",
    "TwentyFiveGig": "TwentyFiveGigE",
    "TF": "TwentyFiveGigE",
    "Tf": "TwentyFiveGigE",
    "tf": "TwentyFiveGigE",
    "TwoHundredGigabitEthernet": "TwoHundredGigabitEthernet",
    "TwoHundredGigEthernet": "TwoHundredGigabitEthernet",
    "TwoHundredGigEth": "TwoHundredGigabitEthernet",
    "TwoHundredGigE": "TwoHundredGigabitEthernet",
    "TwoHundredGig": "TwoHundredGigabitEthernet",
    "TH": "TwoHundredGigabitEthernet",
    "Th": "TwoHundredGigabitEthernet",
    "th": "TwoHundredGigabitEthernet",
    "FourHundredGigabitEthernet": "FourHundredGigabitEthernet",
    "FourHundredGigEthernet": "FourHundredGigabitEthernet",
    "FourHundredGigEth": "FourHundredGigabitEthernet",
    "FourHundredGigE": "FourHundredGigabitEthernet",
    "FourHundredGig": "FourHundredGigabitEthernet",
    "F": "FourHundredGigabitEthernet",
    "f": "FourHundredGigabitEthernet",
    "Loopback": "Loopback",
    "loopback": "Loopback",
    "Lo": "Loopback",
    "lo": "Loopback",
    "Management": "Management",
    "Mgmt": "Management",
    "mgmt": "Management",
    "Ma": "Management",
    "Management_short": "Ma",
    "MFR": "MFR",
    "Multilink": "Multilink",
    "Mu": "Multilink",
    "n": "nve",
    "nv": "nve",
    "nve": "nve",
    "PortChannel": "Port-channel",
    "Port-channel": "Port-channel",
    "Port-Channel": "Port-channel",
    "port-channel": "Port-channel",
    "po": "Port-channel",
    "Po": "Port-channel",
    "POS": "POS",
    "PO": "POS",
    "Serial": "Serial",
    "Se": "Serial",
    "S": "Serial",
    "Sync": "Sync",
    "Sy": "Sync",
    "Ten-GigabitEthernet": "TenGigabitEthernet",
    "TenGigabitEthernet": "TenGigabitEthernet",
    "TenGigEthernet": "TenGigabitEthernet",
    "TenGigEth": "TenGigabitEthernet",
    "TenGig": "TenGigabitEthernet",
    "TeGig": "TenGigabitEthernet",
    "Ten": "TenGigabitEthernet",
    "T": "TenGigabitEthernet",
    "Te": "TenGigabitEthernet",
    "te": "TenGigabitEthernet",
    "Tunnel": "Tunnel",
    "Tun": "Tunnel",
    "Tu": "Tunnel",
    "Twe": "TwentyFiveGigE",
    "Tw": "TwoGigabitEthernet",
    "Two": "TwoGigabitEthernet",
    "Virtual-Access": "Virtual-Access",
    "Vi": "Virtual-Access",
    "Virtual-Template": "Virtual-Template",
    "Vt": "Virtual-Template",
    "VLAN": "VLAN",
    "V": "VLAN",
    "Vl": "VLAN",
    "Vlan-interface": "VLAN",
    "vlan": "VLAN",
    "Wlan-GigabitEthernet": "Wlan-GigabitEthernet",
    "XGE": "TenGigabitEthernet",
}

# The default mac format
DEFAULT_MAC_FORMAT = "MAC_DOT_FOUR"

# A dictionary to describe the MAC format to it's characteristics.
MAC_CREATE = dict(
    MAC_COLON_TWO={"count": 2, "char": ":"},
    MAC_COLON_FOUR={"count": 4, "char": ":"},
    MAC_DASH_TWO={"count": 2, "char": "-"},
    MAC_DASH_FOUR={"count": 4, "char": "-"},
    MAC_DOT_TWO={"count": 2, "char": "."},
    MAC_DOT_FOUR={"count": 4, "char": "."},
    MAC_NO_SPECIAL={"count": 12, "char": ""},
)

# A dictionary to describe the MAC format REGEX pattern.
MAC_REGEX = dict(
    MAC_COLON_TWO=r"([a-fA-F0-9]{2}[:]){5}([a-fA-F0-9]{2})",
    MAC_COLON_FOUR=r"([a-fA-F0-9]{4}[:]){2}([a-fA-F0-9]{4})",
    MAC_DASH_TWO=r"([a-fA-F0-9]{2}[\-]){5}([a-fA-F0-9]{2})",
    MAC_DASH_FOUR=r"([a-fA-F0-9]{4}[\-]){2}([a-fA-F0-9]{4})",
    MAC_DOT_TWO=r"([a-fA-F0-9]{2}[\.]){5}([a-fA-F0-9]{2})",
    MAC_DOT_FOUR=r"([a-fA-F0-9]{4}[\.]){2}([a-fA-F0-9]{4})",
    MAC_NO_SPECIAL=r"([a-fA-F0-9]{12})",
)

"""Variable definitions used in project, purposely not constants to signal to use these variables can be overridden."""

# This variable maps a full interface name, to an opinionated shortened name.
REVERSE_MAPPING = {
    "AppGigabitEthernet": "Ap",
    "ATM": "At",
    "EOBC": "EO",
    "Ethernet": "Et",
    "FastEthernet": "Fa",
    "Fddi": "FD",
    "FortyGigabitEthernet": "Fo",
    "GigabitEthernet": "Gi",
    "HundredGigabitEthernet": "Hu",
    "Loopback": "Lo",
    "Management": "Ma",
    "MFR": "MFR",
    "Multilink": "Mu",
    "Port-channel": "Po",
    "POS": "PO",
    "Serial": "Se",
    "Sync": "Sy",
    "TenGigabitEthernet": "Te",
    "Tunnel": "Tu",
    "TwoGigabitEthernet": "Tw",
    "TwentyFiveGigE": "Twe",
    "Virtual-Access": "Vi",
    "Virtual-Template": "Vt",
    "VLAN": "Vl",
    "Wlan-GigabitEthernet": "Wl-Gi",
}

# These are base level filters to provide documentation of how a CLEAN_FILTER can be used, This is a private variable, and subject
# to change without notice between revisions.
_PROVIDED_CLEAN_FILTERS = [
    {"regex": r"^Current\s+configuration.*\n"},
    {"regex": r"^Building\s+configuration.*\n"},
    {"regex": r"^ntp\s+clock-period.*\n"},
]

# These are base level filters to provide documentation of how a SANITIZE_FILTERS can be used, This is a private variable, and subject
# to change without notice between revisions.
_PROVIDED_SANITIZE_FILTERS = [
    {"regex": r"(username\s+\S+\spassword\s+5\s+)\S+(\s+role\s+\S+)", "replace": "\\1<redacted_config>\\2"},
    {"regex": r"(username\s+\S+\s+privilege\s+15\s+password\s+0\s+)\S+", "replace": "\\1<redacted_config>"},
]

# {0xffffffff ^ ((1 << i) - 1) for i in range(32)}
IPV4_MASKS = {
    4294967168,
    4294967040,
    4294966784,
    4294966272,
    4294965248,
    4294963200,
    4294959104,
    4294950912,
    4294934528,
    4294901760,
    4294836224,
    4294705152,
    4294443008,
    4293918720,
    4292870144,
    4290772992,
    4286578688,
    4278190080,
    4261412864,
    4227858432,
    4160749568,
    4026531840,
    3758096384,
    3221225472,
    2147483648,
    4294967232,
    4294967264,
    4294967280,
    4294967288,
    4294967292,
    4294967294,
    4294967295,
}

# {0xffffffffffffffffffffffffffffffff ^ ((1 << i) - 1) for i in range(128)}
IPV6_MASKS = {
    340282366920938463463374607431768211392,
    340282366920938463315800654842091798528,
    340282366911034943149091565232575217664,
    340282366920938463463374607431768178688,
    340282366920938463463374607431768211424,
    340282366920938463389587631136930004992,
    340282366920938425684442744474606501888,
    340282366920938463463374607431768195072,
    170141183460469231731687303715884105728,
    340282366920938463463374607431768211440,
    340282366920938463426481119284349108224,
    340282366920938463461068764422554517504,
    340282366920938463463374325956791500800,
    340282366920938463463374044481814790144,
    340282366920938463463373481531861368832,
    340282366920938463463374607431767687168,
    340282366920938463463374607431767162880,
    340282366920938463444927863358058659840,
    340282366920938463463374607431766114304,
    340282366920938463463374607431764017152,
    340282366920938463463374607431759822848,
    340282366920938463454151235394913435648,
    340282366920938444573908675953187356672,
    340282366920938463458762921413340823552,
    340282366920938463463370103832140840960,
    340282366920938463463365600232513470464,
    340282366920938463463356593033258729472,
    340282366920938463463338578634749247488,
    340282366920938463463302549837730283520,
    340282366920938463463374607156890304512,
    340282366920938463463374606882012397568,
    340282366920938463463374606332256583680,
    340282366920938463463374605232744955904,
    340282366920938463463374603033721700352,
    340282366920938463463374607431633993728,
    340282366920628978453553262363043430400,
    340282366920928792056817690398370562048,
    340282366881324382206242438634996236288,
    340282366841710300949110269838224261120,
    340282366762482138434845932244680310784,
    340282366604025813406317257057592410112,
    340282366287113163349259906683416608768,
    340282365653287863235145205935065006080,
    340282364385637263006915804438361800704,
    340282361850336062550457001444955389952,
    340282356779733661637539395458142568448,
    340282346638528859811704183484516925440,
    340282366920783720958463934897405820928,
    340282326356119256160033759537265639424,
    340282285791300048856692911642763067392,
    340282204661661634250011215853757923328,
    340282042402384805036647824275747635200,
    340281717883831146609921041119727058944,
    340281068846723829756467474807685906432,
    340279770772509196049560342183603601408,
    340277174624079928635746076935438991360,
    340271982327221393808117546439109771264,
    340261597733504324152860485446451331072,
    340282366920933627760096148915069386752,
    340282366920938463463374607431768207360,
    340282366920938454018641641692477784064,
    340282366920861092210919271164587016192,
    340282366920899777837146939298177613824,
    340282366920936045611735378173418799104,
    340282366920938463463374607427473244160,
    340282366920938463463374607423178276864,
    340282366920938463463374607414588342272,
    340282366920938463463374607397408473088,
    340282366920938463463374607363048734720,
    340282366920938463463374607294329257984,
    340282366920937254537554992802593505280,
    340282366919700523424089227156869087232,
    340282366918462583384803846881969963008,
    340282366915986703306233086332171714560,
    255211775190703847597530955573826158592,
    340282366920938463463374607431751434240,
    340282366920938463463374607431734657024,
    340282366920938463463374607431701102592,
    340282366920938463463374607431768211455,
    340282366920938463463374607431768209408,
    340282366920938463463372355631954526208,
    340282366920938463463374607431499776000,
    340282366920938463463374607431231340544,
    340282366920938463463374607430694469632,
    340282366920938463463374607429620727808,
    340282366920938458741008124562122997760,
    340282366920938463463374607431768211448,
    297747071055821155530452781502797185024,
    340282366920938463463374607431768210432,
    340282366920938461102191365996945604608,
    340282366920938463463374607431768203264,
    340282366920938463463374607431768210944,
    340282366920938463463374607431768211452,
    340282366920938462282782986714356908032,
    319014718988379809496913694467282698240,
    340282366920938463463374607431767949312,
    340282366920937859000464800117180858368,
    340282366920938463463374607431768211454,
    329648542954659136480144150949525454848,
    340282366920938463463374598635675189248,
    340282366920938463463374589839582167040,
    340282366920938463463374572247396122624,
    340282366920938463463374537063024033792,
    340282366920938463463374466694279856128,
    340282366920938387905510881517444792320,
    340282366920938463463230492243692355584,
    340282366920938463463086377055616499712,
    340282366920938463462798146679464787968,
    340282366920938463462221685927161364480,
    340282366920938462873078797073062559744,
    340282366920938463463374607431768211200,
    340240828546070184842346363461134450688,
    340199290171201906221318119490500689920,
    340116213421465348979261631549233168384,
    339950059921992234495148655666698125312,
    339617752923046005526922703901628039168,
    338953138925153547590470800371487866880,
    337623910929368631717566993311207522304,
    334965454937798799971759379190646833152,
    340282366901131422834808523033382223872,
    340282366920938463463374607431768080384,
    340282366920938161231919703774474534912,
    340282366920938463168226702252415385600,
    340282366920938463463374607431768211328,
    340282366920319493443731917294318649344,
    340282366920938463463374607431768145920,
    340282366920938312347647155603121373184,
    340282366920919120650260773364972912640,
}

# End of Text characters for banner
ETX_HEX = "\x03"
CARET_C = "^C"
CARET = "^"

TIME_MAPPINGS = (
    ("years", 31536000),
    ("weeks", 604800),
    ("days", 86400),
    ("hours", 3600),
    ("minutes", 60),
    ("seconds", 1),
)

UPTIME_REGEX_PATTERNS = [
    (
        r"((?P<years>\d+) year(s)?,\s+)?((?P<weeks>\d+) week(s)?,\s+)?"
        r"((?P<days>\d+) day(s)?,\s+)?((?P<hours>\d+) "
        r"hour(s)?,\s+)?((?P<minutes>\d+) minute(s)?)"
    ),
    (
        r"((?P<days>\d+) day(s)?,\s+)?"
        r"((?P<hours>\d+)):((?P<minutes>\d+)):((?P<seconds>\d+))"  # pylint: disable=implicit-str-concat
    ),
    (
        r"(((?P<years>\d+)y)?(?P<weeks>\d+)w)?((?P<days>\d+)d)?((?P<hours>\d+)h)?"
        r"((?P<minutes>\d+)m)?((?P<seconds>\d+)s)"
    ),  # pylint: disable=implicit-str-concat
]
