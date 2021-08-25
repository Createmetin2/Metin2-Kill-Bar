//Find
			Set(HEADER_GC_PING,			CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCPing), STATIC_SIZE_PACKET));
			
///Add
#if defined(__BL_KILL_BAR__)
			Set(HEADER_GC_KILLBAR, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCKillBar), STATIC_SIZE_PACKET));
#endif