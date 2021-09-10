//Find
			CGuildManager::instance().Kill(pkKiller, this);
			
///Add
#if defined(__BL_KILL_BAR__)
			TPacketGCKillBar kb;
			
			kb.bHeader = HEADER_GC_KILLBAR;
			kb.bKillerRace = static_cast<BYTE>(pkKiller->GetRaceNum());
			LPITEM KillerWeapon = pkKiller->GetWear(WEAR_WEAPON);
			kb.bKillerWeaponType = KillerWeapon ? KillerWeapon->GetSubType() : 255;
			kb.bVictimRace = static_cast<BYTE>(GetRaceNum());

			strlcpy(kb.szKiller, pkKiller->GetName(), sizeof(kb.szKiller));
			strlcpy(kb.szVictim, GetName(), sizeof(kb.szVictim));

			const DESC_MANAGER::DESC_SET& c_set_desc = DESC_MANAGER::instance().GetClientSet();
			for (DESC_MANAGER::DESC_SET::const_iterator it = c_set_desc.begin(); it != c_set_desc.end(); ++it)
			{
				LPDESC d_c = *it;
				if (!d_c)
					continue;

				LPCHARACTER c_c = d_c->GetCharacter();
				if (!c_c)
					continue;

				if (pkKiller->GetMapIndex() != c_c->GetMapIndex())
					continue;

				d_c->Packet(&kb, sizeof(kb));
			}
#endif
