#!/usr/bin/env python3
import json, shutil, sys
from pathlib import Path

src = Path(sys.argv[1])
manifest = Path(sys.argv[2] if len(sys.argv) > 2 else "AssetManifest.json")
out = Path(sys.argv[3] if len(sys.argv) > 3 else "assets")
out.mkdir(exist_ok=True)
if not src.is_dir():
    sys.exit(1)

NEEDED = ["register_start_illustration.png", "register_email_illustration.png",
          "register_pin_illustration.png", "register_done_illustration.png",
          "supercell_id_logo_white.png", "id_logo.png", "id_logo_black.png",
          "avatar_chicken.png", "avatar_spike.png", "avatar_princess.png", "avatar_el_primo.png",
          "avatar_barb.png", "avatar_hog_rider.png", "settings_cogwheel.png",
          "messages_bubble.png", "friend_face_icon.png", "friend_face_icon_grayscale.png",
          "tab_icon_star_disabled.png", "tab_icon_star.png", "tab_icon_sword_disabled.png",
          "logo_small_laser.png", "AppIcon_laser.png", "AppIcon_magic.png",
          "AppIcon_scroll.png", "AppIcon_soil.png", "AppIcon_squad.png",
          "login_email_illustration.png",
          "avatar_archer.png", "avatar_barb.png", "avatar_bazooka.png", "avatar_chicken.png", "avatar_dr_t.png", "avatar_el_primo.png", "avatar_heavy.png", "avatar_hog_rider.png", "avatar_king.png", "avatar_mortis.png", "avatar_pig.png", "avatar_princess.png", "avatar_ram_rider.png", "avatar_spike.png", "avatar_moco_ellie.png", "avatar_moco_jax.png", "avatar_moco_luna.png", "avatar_moco_manny.png", "avatar_moco_sniffer_dog.png", "avatar_moco_support_cat.png", "tab_icon_face_blue.png", "tab_icon_face_red.png", "tab_icon_face_disabled.png", "tab_icon_sword.png", "tab_icon_sword_disabled.png", "switch_account_icon.png", "log_out_icon.png", "account_protection_icon_disabled.png", "ui_icon_external_link.png"]

files = json.load(open(manifest))["RemoteAssets"]["iOS"]["images3x"]
index = {p.stem: p for p in src.rglob("*") if p.is_file()}
index.update({p.name: p for p in src.rglob("*") if p.is_file()})

for name in NEEDED:
    h = files.get(name)
    if not h:
        continue
    p = index.get(h) or index.get(name)
    if p:
        shutil.copy(p, out / name)

AUDIO = ["cancel_btn_01.m4a", "generic_button_01.m4a", "new_game_02.m4a",
         "pop_up_window_close_01.m4a", "pop_up_window_open_01.m4a",
         "sign_in_checkmark_sfx_01.m4a", "switching_tabs_jump_02.m4a"]
audio = json.load(open(manifest))["RemoteAssets"]["iOS"]["Audio"]
for name in AUDIO:
    h = audio.get(name)
    if not h:
        continue
    p = index.get(h) or index.get(name)
    if p:
        shutil.copy(p, out / name)
