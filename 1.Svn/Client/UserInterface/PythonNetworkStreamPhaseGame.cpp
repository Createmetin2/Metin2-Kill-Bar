//Find
			case HEADER_GC_SHOP:
				ret = RecvShopPacket();
				break;
				
///Add
#if defined(__BL_KILL_BAR__)
			case HEADER_GC_KILLBAR:
				ret = RecvKillBar();
				break;
#endif

//Find
bool CPythonNetworkStream::RecvCharacterPositionPacket()
{
	...
}

///Add
#if defined(__BL_KILL_BAR__)
bool CPythonNetworkStream::RecvKillBar()
{
	TPacketGCKillBar p;

	if (!Recv(sizeof(p), &p))
		return false;

	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "AddKillInfo", 
		Py_BuildValue("(ssiii)", p.szKiller, p.szVictim, p.bKillerRace, p.bVictimRace, p.bKillerWeaponType));

	return true;
}
#endif