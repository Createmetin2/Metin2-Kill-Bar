#Add
if app.BL_KILL_BAR:
	import playersettingmodule
	import item

#Find
	CANNOT_SEE_INFO_MAP_DICT = {
		"metin2_map_monkeydungeon" : False,
		"metin2_map_monkeydungeon_02" : False,
		"metin2_map_monkeydungeon_03" : False,
		"metin2_map_devilsCatacomb" : False,
	}

#Add
	if app.BL_KILL_BAR:
		KILL_BAR_COOLTIME = 4.0
		KILL_BAR_MOVE_SPEED = 3.0
		KILL_BAR_MOVE_DISTANCE = 33.0
		KILL_BAR_MAX_ITEM = 5

		KILL_BAR_RACE = {
			playersettingmodule.RACE_WARRIOR_M: "|Ekill_bar/warrior_m|e",
			playersettingmodule.RACE_ASSASSIN_W	: "|Ekill_bar/assassin_w|e",
			playersettingmodule.RACE_SURA_M		: "|Ekill_bar/sura_m|e",
			playersettingmodule.RACE_SHAMAN_W	: "|Ekill_bar/shaman_w|e",
			playersettingmodule.RACE_WARRIOR_W	: "|Ekill_bar/warrior_w|e",
			playersettingmodule.RACE_ASSASSIN_M	: "|Ekill_bar/assassin_m|e",
			playersettingmodule.RACE_SURA_W		: "|Ekill_bar/sura_w|e",
			playersettingmodule.RACE_SHAMAN_M	: "|Ekill_bar/shaman_m|e",
		}

		KILL_BAR_WEAPON_TYPE = {
			"FIST": "|Ekill_bar/fist|e",
			item.WEAPON_SWORD: "|Ekill_bar/sword|e",
			item.WEAPON_DAGGER: "|Ekill_bar/dagger|e",
			item.WEAPON_BOW: "|Ekill_bar/bow|e",
			item.WEAPON_TWO_HANDED: "|Ekill_bar/twohand|e",
			item.WEAPON_BELL: "|Ekill_bar/bell|e",
			item.WEAPON_FAN: "|Ekill_bar/fan|e",
		}

#Find
		self.serverInfo = None

#Add
		if app.BL_KILL_BAR:
			self.KillList = list()

#Find
	def Close(self):
		self.HideMiniMap()

#Add
	if app.BL_KILL_BAR:
		def RepositionKillBar(self, obj):
			obj["MOVE_Y"] += MiniMap.KILL_BAR_MOVE_DISTANCE
			return obj

		def AddKillInfo(self, killer, victim, killer_race, victim_race, weapon_type):
			if len(self.KillList) >= MiniMap.KILL_BAR_MAX_ITEM:
				self.KillList.sort(
					key=lambda obj: obj["CoolTime"], reverse=True)
				del self.KillList[-1]
			
			if self.KillList:
				self.KillList = map(self.RepositionKillBar, self.KillList)

			TBoard = ui.ThinBoard()
			TBoard.SetParent(self)
			TBoard.SetSize(155, 10)
			TBoard.SetPosition(15, 185)
			TBoard.Show()

			KillText = ui.TextLine()
			KillText.SetText("{} {} {} {} {}".format(MiniMap.KILL_BAR_RACE.get(int(killer_race), ""), killer, MiniMap.KILL_BAR_WEAPON_TYPE.get(
				int(weapon_type), MiniMap.KILL_BAR_WEAPON_TYPE.get("FIST")), victim, MiniMap.KILL_BAR_RACE.get(int(victim_race), "")))
			KillText.SetParent(TBoard)
			KillText.SetWindowHorizontalAlignCenter()
			KillText.SetWindowVerticalAlignCenter()
			KillText.SetHorizontalAlignCenter()
			KillText.SetVerticalAlignCenter()
			KillText.Show()

			KillDict = dict()
			KillDict["ThinBoard"] = TBoard
			KillDict["TextLine"] = KillText
			KillDict["CoolTime"] = app.GetTime() + MiniMap.KILL_BAR_COOLTIME
			KillDict["DELETE"] = False
			KillDict["MOVE_X"] = MiniMap.KILL_BAR_MOVE_DISTANCE
			KillDict["MOVE_Y"] = 0.0

			self.KillList.append(KillDict)

#Find
		self.AtlasWindow = None

#Add
		if app.BL_KILL_BAR:
			self.KillList = None

#Find
		if True == self.AtlasShowButton.IsIn():
			self.tooltipAtlasOpen.Show()
		else:
			self.tooltipAtlasOpen.Hide()

#Add
		if app.BL_KILL_BAR:
			if self.KillList:
				self.KillList = filter(
					lambda obj: obj["CoolTime"] > app.GetTime(), self.KillList)
				for obj in self.KillList:
					(xLocal, yLocal) = obj["ThinBoard"].GetLocalPosition()
					if obj["MOVE_X"] > 0.0:
						obj["ThinBoard"].SetPosition(xLocal - MiniMap.KILL_BAR_MOVE_SPEED, yLocal)
						obj["MOVE_X"] -= MiniMap.KILL_BAR_MOVE_SPEED
					if obj["MOVE_Y"] > 0.0:
						obj["ThinBoard"].SetPosition(xLocal, yLocal + MiniMap.KILL_BAR_MOVE_SPEED)
						obj["MOVE_Y"] -= MiniMap.KILL_BAR_MOVE_SPEED