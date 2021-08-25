//Find
	HEADER_GC_RESPOND_CHANNELSTATUS			= 210,
	
///Add
#if defined(__BL_KILL_BAR__)
	HEADER_GC_KILLBAR 						= 218,
#endif

//Find
typedef struct packet_channel
{
	...
} TPacketGCChannel;

///Add
#if defined(__BL_KILL_BAR__)
typedef struct command_kill_bar
{
	BYTE	bHeader;
	BYTE	bKillerRace;
	BYTE	bKillerWeaponType;
	BYTE	bVictimRace;
	char	szKiller[CHARACTER_NAME_MAX_LEN + 1];
	char	szVictim[CHARACTER_NAME_MAX_LEN + 1];
} TPacketGCKillBar;
#endif