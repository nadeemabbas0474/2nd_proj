# Running Safe-HIL-RL on Google Colab

## 📦 What's Included

This package contains everything you need to run the Safe Human-in-the-Loop RL project on Google Colab after your remote GPU connection broke.

### Files:

1. **Safe_HIL_RL_Colab_Setup.ipynb** - Complete Jupyter notebook with step-by-step setup
2. **colab_helper_script.py** - Python helper utilities for managing the project
3. **COLAB_SETUP_GUIDE.md** - Detailed setup guide with explanations
4. **QUICK_REFERENCE.md** - Quick reference card with copy-paste commands
5. **README_COLAB.md** - This file

## 🚀 Getting Started (3 Options)

### Option 1: Use the Jupyter Notebook (Easiest)

**Best for:** First-time users, complete guided setup

1. Go to [Google Colab](https://colab.research.google.com/)
2. Upload `Safe_HIL_RL_Colab_Setup.ipynb`
3. Enable GPU: `Runtime` → `Change runtime type` → `GPU`
4. Run cells from top to bottom
5. Follow the instructions in each cell

**Time:** 20-30 minutes for complete setup

### Option 2: Quick Setup (Fastest)

**Best for:** Experienced users who want to start quickly

1. Open [Google Colab](https://colab.research.google.com/)
2. Create new notebook
3. Enable GPU
4. Copy-paste the "One-Command Setup" from `QUICK_REFERENCE.md`
5. Run and wait for completion

**Time:** 15-20 minutes

### Option 3: Manual Setup (Most Control)

**Best for:** Users who want to understand each step

1. Follow the step-by-step guide in `COLAB_SETUP_GUIDE.md`
2. Execute each command manually
3. Customize as needed

**Time:** 30-40 minutes

## 📋 Prerequisites

- Google account
- Basic understanding of Python and Jupyter notebooks
- The original repository: https://github.com/OscarHuangWind/Safe-Human-in-the-Loop-RL

## ⚡ Quick Start Command

If you just want to get started immediately, run this in a new Colab notebook with GPU enabled:

```python
# Complete setup in one cell
!apt-get update -qq && apt-get install -y -qq libspatialindex-dev xorg libx11-dev libglu1-mesa-dev libgl1-mesa-dev xvfb ffmpeg
!pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
!pip install -q numpy pandas matplotlib seaborn gym gymnasium pyyaml tensorboard opencv-python pillow scipy scikit-learn pyvirtualdisplay

import os
os.chdir("/content")
!git clone https://github.com/OscarHuangWind/Safe-Human-in-the-Loop-RL.git
!git clone https://github.com/huawei-noah/SMARTS.git

os.chdir("/content/SMARTS")
!git checkout comp-1
!pip install -q -e '.[camera_obs,test,train]' && pip install -q -e '.[extras]'

os.chdir("/content/Safe-Human-in-the-Loop-RL")
!scl scenario build --clean scenario/straight/

from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()

import sys
sys.path.insert(0, "/content/SMARTS")
sys.path.insert(0, "/content/Safe-Human-in-the-Loop-RL")

print("✓ Setup complete! Ready to train.")
```

Then start training:

```python
!python main.py
```

## 🎯 What Works on Colab

✅ **Training base models** (without human guidance)  
✅ **Evaluation** of trained models  
✅ **GPU acceleration** (T4, V100, A100)  
✅ **TensorBoard** visualization  
✅ **Saving/loading** checkpoints  
✅ **Google Drive** integration  

## ⚠️ What Doesn't Work

❌ **Human guidance features** (keyboard/G29 steering wheel)  
❌ **Envision visualization** (localhost:8081)  
❌ **Real-time interaction** during training  

### Workaround:
1. Train base models on Colab
2. Download trained models
3. Continue with human guidance on local machine

## 💾 Saving Your Work

**IMPORTANT:** Colab sessions can disconnect! Always save to Google Drive:

```python
# Mount Drive
from google.colab import drive
drive.mount('/content/drive')

# Save progress
!cp -r logs/ /content/drive/MyDrive/SafeHIL_Results/
!cp -r models/ /content/drive/MyDrive/SafeHIL_Results/
!cp -r checkpoints/ /content/drive/MyDrive/SafeHIL_Results/
```

## 🔄 Recovering After Disconnect

If your session disconnects:

```python
# 1. Mount Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. Load progress
os.chdir("/content/Safe-Human-in-the-Loop-RL")
!cp -r /content/drive/MyDrive/SafeHIL_Results/* ./

# 3. Fix paths
import sys
sys.path.insert(0, "/content/SMARTS")
sys.path.insert(0, "/content/Safe-Human-in-the-Loop-RL")

# 4. Continue training
!python main.py
```

## 📊 Monitoring Training

### TensorBoard
```python
%load_ext tensorboard
%tensorboard --logdir logs/
```

### Check GPU
```python
!nvidia-smi
```

### View Logs
```python
!tail -50 logs/training.log
```

## 🐛 Common Issues

### Issue: CUDA Out of Memory
**Solution:** Reduce batch size in config.yaml

### Issue: Module Not Found
**Solution:** Re-run path setup:
```python
import sys
sys.path.insert(0, "/content/SMARTS")
sys.path.insert(0, "/content/Safe-Human-in-the-Loop-RL")
```

### Issue: Session Timeout
**Solution:** Save to Google Drive regularly

See `COLAB_SETUP_GUIDE.md` for more troubleshooting.

## 📚 Documentation

- **Safe_HIL_RL_Colab_Setup.ipynb** - Interactive notebook with all steps
- **COLAB_SETUP_GUIDE.md** - Comprehensive guide with explanations
- **QUICK_REFERENCE.md** - Quick commands for common tasks
- **colab_helper_script.py** - Utility functions for automation

## 🎓 Recommended Workflow

1. **Setup** (20 min): Run the Jupyter notebook
2. **Test** (5 min): Train for 1-2 epochs to verify
3. **Train** (1-8 hours): Full training run
4. **Save** (2 min): Copy results to Google Drive
5. **Download** (5 min): Download models locally
6. **Continue** (local): Human guidance on local machine

## 💡 Tips

1. **Enable GPU first** - Always check GPU is enabled
2. **Save frequently** - Every 10-20 epochs to Drive
3. **Monitor memory** - Use `!nvidia-smi` to check
4. **Start small** - Test with few epochs first
5. **Use Colab Pro** - For longer sessions and better GPUs

## 🆘 Need Help?

1. Check `COLAB_SETUP_GUIDE.md` troubleshooting section
2. Review `QUICK_REFERENCE.md` for common commands
3. Check error messages carefully
4. Verify all dependencies are installed

## 📈 Performance

### Free Colab:
- GPU: T4 (16GB)
- Session: 12 hours max
- Idle timeout: 90 minutes
- Good for: Testing, small experiments

### Colab Pro:
- GPU: V100/A100 (better)
- Session: 24 hours max
- Idle timeout: Longer
- Good for: Full training runs

## 🔗 Links

- [Original Repository](https://github.com/OscarHuangWind/Safe-Human-in-the-Loop-RL)
- [SMARTS Simulator](https://github.com/huawei-noah/SMARTS)
- [Google Colab](https://colab.research.google.com/)
- [Colab FAQ](https://research.google.com/colaboratory/faq.html)

## 📝 Notes

- This setup is specifically designed for Colab environment
- Human guidance features require local setup
- Always save important results to Google Drive
- Free tier has usage limits
- GPU availability not guaranteed on free tier

## 🎉 Success Checklist

Before starting training, verify:

- [ ] GPU is enabled and detected
- [ ] All dependencies installed successfully
- [ ] SMARTS installed and importable
- [ ] Scenario built successfully
- [ ] Virtual display started
- [ ] Python paths configured
- [ ] Google Drive mounted (recommended)
- [ ] Config.yaml exists and is correct

## 🚦 Next Steps

After setup:

1. **Test**: Run 1-2 epochs to verify everything works
2. **Train**: Start full training run
3. **Monitor**: Check progress with TensorBoard
4. **Save**: Regularly save to Google Drive
5. **Evaluate**: Switch to evaluation mode and test
6. **Download**: Get trained models for local use

---

**Ready to start? Open `Safe_HIL_RL_Colab_Setup.ipynb` in Google Colab!** 🚀

Good luck with your training! If you encounter any issues, refer to the detailed guides included in this package.
