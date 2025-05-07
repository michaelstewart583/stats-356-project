
import os
from PIL import Image



# 1) CONFIGURE THESE
SRC_DIR  = "./img_align_celeba"
DST_DIR  = "./img_align_celeba_small"
NEW_SIZE = (64, 64)   # change to (32, 32) if you prefer

# 2) Walk source tree
for root, dirs, files in os.walk(SRC_DIR):
    # Compute corresponding destination directory
    rel_path = os.path.relpath(root, SRC_DIR)
    target_dir = os.path.join(DST_DIR, rel_path)
    os.makedirs(target_dir, exist_ok=True)

    for fname in files:
        # skip non-image files by extension
        if not fname.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
            continue

        src_path = os.path.join(root, fname)
        dst_path = os.path.join(target_dir, fname)

        try:
            # open, convert to RGB (drops alpha), resize, and save
            with Image.open(src_path) as img:
                img = img.convert("RGB")          # ensure 3 channels
                img = img.resize(NEW_SIZE, Image.LANCZOS)
                img.save(dst_path, quality=95)    # you can tweak quality
        except Exception as e:
            print(f"⚠️ Skipping {src_path}: {e}")

print("✅ All done! Your resized images are in:", DST_DIR)
