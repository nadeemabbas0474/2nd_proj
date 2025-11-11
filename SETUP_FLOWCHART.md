# Safe-HIL-RL Colab Setup Flowchart

## 🗺️ Complete Setup Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    START: Google Colab                       │
│                                                              │
│  1. Go to https://colab.research.google.com/                │
│  2. Upload Safe_HIL_RL_Colab_Setup.ipynb                    │
│     OR create new notebook                                   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 1: Enable GPU Runtime                      │
│                                                              │
│  Runtime → Change runtime type → GPU → Save                 │
│                                                              │
│  ✓ Verify: !nvidia-smi                                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 2: Install System Dependencies                  │
│                                                              │
│  • libspatialindex-dev                                       │
│  • xorg, libx11-dev, mesa libraries                         │
│  • xvfb, ffmpeg                                             │
│                                                              │
│  Time: ~3-5 minutes                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 3: Install PyTorch with CUDA                    │
│                                                              │
│  pip install torch torchvision torchaudio                    │
│                                                              │
│  ✓ Verify: torch.cuda.is_available()                        │
│  Time: ~2-3 minutes                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 4: Clone Repositories                           │
│                                                              │
│  1. Safe-Human-in-the-Loop-RL                               │
│  2. SMARTS (checkout comp-1 branch)                         │
│                                                              │
│  Time: ~2-3 minutes                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 5: Install Python Dependencies                  │
│                                                              │
│  • numpy, pandas, matplotlib                                 │
│  • gym, gymnasium, pyyaml                                    │
│  • opencv-python, pillow, scipy                             │
│  • tensorboard                                               │
│                                                              │
│  Time: ~3-5 minutes                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 6: Install SMARTS Simulator                     │
│                                                              │
│  pip install -e '.[camera_obs,test,train]'                  │
│  pip install -e '.[extras]'                                 │
│                                                              │
│  ✓ Verify: import smarts                                    │
│  Time: ~5-8 minutes                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 7: Build Scenario                               │
│                                                              │
│  scl scenario build --clean scenario/straight/              │
│                                                              │
│  Time: ~2-5 minutes                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 8: Setup Virtual Display                        │
│                                                              │
│  Display(visible=0, size=(1400, 900))                       │
│                                                              │
│  Time: ~1 minute                                             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 9: Configure Python Paths                       │
│                                                              │
│  sys.path.insert(0, "/content/SMARTS")                      │
│  sys.path.insert(0, "/content/Safe-Human-in-the-Loop-RL")  │
│                                                              │
│  Time: <1 minute                                             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│    OPTIONAL: Mount Google Drive (HIGHLY RECOMMENDED)         │
│                                                              │
│  drive.mount('/content/drive')                              │
│  mkdir -p /content/drive/MyDrive/SafeHIL_Results            │
│                                                              │
│  Time: ~1 minute                                             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              ✓ SETUP COMPLETE!                              │
│                                                              │
│  Total Time: ~20-30 minutes                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
┌──────────────────┐         ┌──────────────────┐
│   TRAINING MODE  │         │ EVALUATION MODE  │
└────────┬─────────┘         └────────┬─────────┘
         │                            │
         ▼                            ▼
┌──────────────────┐         ┌──────────────────┐
│ python main.py   │         │ Edit config.yaml │
│                  │         │ mode=evaluation  │
│ Monitor with:    │         │ python main.py   │
│ • TensorBoard    │         └──────────────────┘
│ • nvidia-smi     │
│ • tail logs/     │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────────────────────────┐
│         Save Progress Every 10 Epochs         │
│                                               │
│  cp -r logs/ /content/drive/MyDrive/...      │
│  cp -r models/ /content/drive/MyDrive/...    │
│  cp -r checkpoints/ /content/drive/MyDrive/  │
└────────┬──────────────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────────────┐
│            Training Complete!                 │
│                                               │
│  • Download results                           │
│  • Continue with human guidance locally       │
└───────────────────────────────────────────────┘
```

## 🔄 Recovery Flow (After Disconnect)

```
┌─────────────────────────────────────────────┐
│      Session Disconnected/Timeout            │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│   Did you save to Google Drive?              │
└──────┬──────────────────────┬────────────────┘
       │ YES                  │ NO
       ▼                      ▼
┌──────────────┐    ┌─────────────────────────┐
│ RECOVERABLE  │    │ START FROM BEGINNING    │
└──────┬───────┘    │ (Lost all progress)     │
       │            └─────────────────────────┘
       ▼
┌──────────────────────────────────────────────┐
│  1. Create new Colab notebook                 │
│  2. Enable GPU                                │
│  3. Mount Google Drive                        │
│  4. Clone repositories                        │
│  5. Install dependencies (quick)              │
│  6. Load saved progress from Drive            │
│  7. Continue training                         │
│                                               │
│  Time: ~10-15 minutes                         │
└───────────────────────────────────────────────┘
```

## 📊 Decision Tree: Which Setup Method?

```
                    START
                      │
                      ▼
        ┌─────────────────────────┐
        │  First time using?      │
        └──────┬──────────┬───────┘
               │ YES      │ NO
               ▼          ▼
    ┌──────────────┐  ┌──────────────────┐
    │ Use Jupyter  │  │ Experienced with │
    │ Notebook     │  │ Colab?           │
    │              │  └────┬─────────┬───┘
    │ EASIEST      │       │ YES     │ NO
    └──────────────┘       ▼         ▼
                    ┌──────────┐  ┌──────────┐
                    │ Quick    │  │ Manual   │
                    │ Setup    │  │ Setup    │
                    │          │  │          │
                    │ FASTEST  │  │ DETAILED │
                    └──────────┘  └──────────┘
```

## 🎯 Training Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    TRAINING WORKFLOW                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: Initial Test (5-10 minutes)                        │
│                                                              │
│  • Run 1-2 epochs                                            │
│  • Verify everything works                                   │
│  • Check GPU utilization                                     │
│  • Monitor memory usage                                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 2: Full Training (1-8 hours)                          │
│                                                              │
│  • Start full training run                                   │
│  • Monitor with TensorBoard                                  │
│  • Save every 10 epochs                                      │
│  • Check logs periodically                                   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 3: Evaluation (10-30 minutes)                         │
│                                                              │
│  • Switch to evaluation mode                                 │
│  • Test trained models                                       │
│  • Analyze results                                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 4: Download & Continue Locally                        │
│                                                              │
│  • Download trained models                                   │
│  • Download logs and checkpoints                             │
│  • Continue with human guidance on local machine             │
└───────────────────────────────────────────────────────────────┘
```

## 🐛 Troubleshooting Decision Tree

```
                    ERROR OCCURRED
                          │
                          ▼
        ┌─────────────────────────────────┐
        │     What type of error?         │
        └──┬──────┬──────┬──────┬────────┘
           │      │      │      │
    ┌──────┘      │      │      └──────┐
    ▼             ▼      ▼             ▼
┌────────┐  ┌────────┐ ┌────────┐ ┌────────┐
│ CUDA   │  │Module  │ │Display │ │Install │
│ OOM    │  │Not     │ │Error   │ │Failed  │
│        │  │Found   │ │        │ │        │
└───┬────┘  └───┬────┘ └───┬────┘ └───┬────┘
    │           │          │          │
    ▼           ▼          ▼          ▼
┌────────┐  ┌────────┐ ┌────────┐ ┌────────┐
│Reduce  │  │Fix     │ │Restart │ │Check   │
│batch   │  │sys.    │ │virtual │ │system  │
│size    │  │path    │ │display │ │deps    │
└────────┘  └────────┘ └────────┘ └────────┘
```

## 📈 Performance Optimization Flow

```
┌─────────────────────────────────────────────┐
│         Training Too Slow?                   │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Check GPU Usage     │
        │  !nvidia-smi         │
        └──────┬───────────────┘
               │
               ▼
        ┌──────────────────────┐
        │  GPU < 80% utilized? │
        └──┬───────────────┬───┘
           │ YES           │ NO
           ▼               ▼
    ┌──────────────┐  ┌──────────────┐
    │ Increase     │  │ Decrease     │
    │ batch size   │  │ batch size   │
    │              │  │ (if OOM)     │
    └──────────────┘  └──────────────┘
```

## 💾 Save Strategy Flow

```
┌─────────────────────────────────────────────┐
│         Training in Progress                 │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Every 10 Epochs     │
        └──────┬───────────────┘
               │
               ▼
        ┌──────────────────────┐
        │  Auto-save to Drive  │
        │  • logs/             │
        │  • models/           │
        │  • checkpoints/      │
        └──────┬───────────────┘
               │
               ▼
        ┌──────────────────────┐
        │  Continue Training   │
        └──────────────────────┘
```

## 🎓 Learning Path

```
┌─────────────────────────────────────────────┐
│  BEGINNER: Start Here                       │
│                                              │
│  1. Read README_COLAB.md                    │
│  2. Use Safe_HIL_RL_Colab_Setup.ipynb       │
│  3. Follow step-by-step                     │
│  4. Train for 1-2 epochs (test)             │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│  INTERMEDIATE: Optimize                      │
│                                              │
│  1. Use QUICK_REFERENCE.md                  │
│  2. Customize config.yaml                   │
│  3. Full training run                       │
│  4. Monitor with TensorBoard                │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│  ADVANCED: Automate                          │
│                                              │
│  1. Use colab_helper_script.py              │
│  2. Auto-save strategies                    │
│  3. Hyperparameter tuning                   │
│  4. Multiple experiments                    │
└───────────────────────────────────────────────┘
```

## 📋 Checklist Flow

```
BEFORE TRAINING:
├─ [ ] GPU enabled and detected
├─ [ ] All dependencies installed
├─ [ ] SMARTS installed successfully
├─ [ ] Scenario built
├─ [ ] Virtual display running
├─ [ ] Python paths configured
├─ [ ] Google Drive mounted
└─ [ ] Config.yaml verified

DURING TRAINING:
├─ [ ] Monitor GPU usage
├─ [ ] Check logs periodically
├─ [ ] Save every 10 epochs
├─ [ ] Watch for errors
└─ [ ] TensorBoard running

AFTER TRAINING:
├─ [ ] Save final results to Drive
├─ [ ] Download models locally
├─ [ ] Backup all checkpoints
├─ [ ] Document hyperparameters
└─ [ ] Prepare for local continuation
```

---

## 🎯 Quick Navigation

- **First Time?** → Use Jupyter Notebook
- **Need Speed?** → Use Quick Setup
- **Want Control?** → Use Manual Setup
- **Got Error?** → Check Troubleshooting Tree
- **Session Died?** → Follow Recovery Flow
- **Training Slow?** → Check Performance Flow

---

**Keep this flowchart handy for reference! 📌**
