#Find
	def __EnableTestServerFlag(self):
		app.EnableTestServerFlag()

#Add
	if app.BL_KILL_BAR:
		def AddKillInfo(self, killer, victim, killer_race, victim_race, weapon_type):
			if self.interface:
				self.interface.AddKillInfo(killer, victim, killer_race, victim_race, weapon_type)