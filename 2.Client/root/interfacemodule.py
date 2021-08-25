#Find
	def ToggleCharacterWindowStatusPage(self):
		self.ToggleCharacterWindow("STATUS")

#Add
	if app.BL_KILL_BAR:
		def AddKillInfo(self, killer, victim, killer_race, victim_race, weapon_type):
			self.wndMiniMap.AddKillInfo(killer, victim, killer_race, victim_race, weapon_type)