//Find
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

///Add
#if defined(__BL_KILL_BAR__)
	PyModule_AddIntConstant(poModule, "BL_KILL_BAR", true);
#else
	PyModule_AddIntConstant(poModule, "BL_KILL_BAR", false);
#endif