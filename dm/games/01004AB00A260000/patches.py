# DARK SOULS: REMASTERED (01004AB00A260000): the rewriter's patches of this game's own builds. dm/tools/patch_nso.py loads every profile's patches.py and applies those of a module's NSO build ID;
# CUTS, OBS and FRAME_STEP as described there ("Registered patches"). Patches of Nintendo SDK module builds are in dm/tools/sdk_patches.py
CUTS = {
  # Dark Souls Remastered 1.0.3 (v196608) main: 60 fps (30 on the Switch). The game presents at interval 1; its render thread (HGCommandDispatcher, main+0x8a4b28) ends each frame in a CPU limiter,
  # main+0x707090(this, fps): 1000 / fps ms less the time since its last call (nn::os::GetSystemTick), slept out when more than 2 ms are left; the main thread waits for the render thread.
  # The 30 is a constant at the only call (main+0x706fa4). The game does not step by the time that passed: the main thread's frame update (main+0x6a337c, on the manager at GOT 0x2287be0)
  # takes a fixed step, the float 1/30 at main+0x167a6ec loaded at main+0x667904, so at 60 fps everything ran twice as fast (on the iPhone). The step loads the 1/60 that rodata holds at
  # main+0x167a834 instead (as the community's 60 fps cheat for this build does). Climbing ladders still misplays at 60 (known with that cheat too). The limiter's frame-skip mode only starts
  # above 36.4 ms a frame, so 60 does not reach it
  'df3766a2bb651a3e822828abf10b6f7b': [
    (0x706fa4, 'e10f1f32', '81078052', 'frame limiter target: mov w1,#30 → mov w1,#60 (main+0x707090 sleeps out 1000 / fps ms since the last frame)'),
    (0x667904, '08ed46bd', '083548bd', 'frame update step: ldr s8,[x8,#0x6ec] (1/30) → ldr s8,[x8,#0x834] (1/60), passed to main+0x6a337c'),
  ],
  # Dark Souls Remastered 1.0.0 (v0) main, the same two changes at this build's own offsets (found by shape: the
  # limiter call site is `mov w1,#30` immediately followed by the call, main+0x7137c8, and the frame update step is
  # the `adrp x8; ldr s8,[x8,#0x970]` pair feeding main+0x6a8480). Unlike 1.0.3 the two float constants are not in the
  # same page here (1/30 at 0x1681970, 1/60 at 0x16839e8), so the adrp page changes as well as the load offset
  '5a797a3a5da6c4f3468cb7c84e4dde63': [
    (0x70b364, 'e10f1f32', 'e10f1e32', 'frame limiter target: mov w1,#30 → mov w1,#60 (main+0x7137c8 sleeps out 1000 / fps ms)'),
    (0x66c9c8, 'a88000b0', 'a88000f0', 'frame update step: adrp x8,#0x1681000 (1/30 page) → adrp x8,#0x1683000 (1/60 page)'),
    (0x66c9cc, '087149bd', '08e949bd', 'frame update step: ldr s8,[x8,#0x970] (1/30) → ldr s8,[x8,#0x9e8] (1/60), passed to main+0x6a8480'),
  ],
}

# How general each patch is and could be (dm/tools/docs_patches.py "Binding", listed in docs/agents/game-patches.md): what, its binding now, the loosest it could have (goal),
# purpose, why; blocked or kept: why the gap stays open (cannot close yet, or left open on purpose); checked: what was checked on game files (else a judgement)
BINDING = [
    {'what': 'frame limiter 30 → 60 fps and the 1/60 update step', 'now': 'build', 'goal': 'game', 'purpose': 'frame rate',
     'why': "the game's own limiter constant and fixed step"},
]
