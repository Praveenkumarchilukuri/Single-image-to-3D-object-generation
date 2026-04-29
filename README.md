# Single Image to 3D Object Generation

This repository contains a pipeline for generating 3D objects from a single image reference. It leverages powerful deep learning models and Neural Radiance Fields (NeRF) to synthesize novel views and extract 3D meshes from 2D input.

## Overview

The pipeline takes a single image as input and produces a 3D representation. It uses image features and textual guidance to guide the 3D generation process.

## 1. Environment Setup

This project essentially requires a GPU with CUDA support (NVIDIA). The dependencies (`tiny-cuda-nn`, `pytorch3d`) rely heavily on custom CUDA kernels.

### Recommended Environment (Conda)
It is highly recommended to use Anaconda or Miniconda to manage dependencies.

```bash
# Create a new environment (Python 3.9 or 3.10 is usually safe for these tools)
conda create -n nerf_env python=3.9
conda activate nerf_env

# Install PyTorch with CUDA support (Check pytorch.org for your specific CUDA version)
# Example for CUDA 11.8:
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

## 2. Installing Complex Dependencies

The description mentions libraries that can be tricky to install:

### tiny-cuda-nn
This is an NVIDIA library for fast neural networks. It often requires compilation.
```bash
pip install git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch
```
*Note: You need a C++ compiler (like Visual Studio Build Tools on Windows) installed for this to work.*

### PyTorch3D
```bash
pip install "git+https://github.com/facebookresearch/pytorch3d.git"
```

### Other Python Libraries
Install the standard AI libraries:
```bash
pip install diffusers transformers accelerate scipy pandas numpy opencv-python trimesh matplotlib
```

## 3. Running the Project

Once the environment is set up, you can run the main pipeline using `main.py`.

### Basic Usage
To generate a 3D object from an image:

```bash
python main.py --ref_path ./image.png --workspace trial_output
```

### Advanced Usage
If you want to provide a specific text description instead of letting the model guess:

```bash
python main.py --ref_path ./image.png --text "A specific description of the object" --workspace trial_output
```

### Exporting
To save the result as a 3D mesh (`.obj`) that you can open in Blender:

```bash
python main.py --ref_path ./image.png --save_mesh
```

## 4. Understanding the Output

- **Workspace Folder**: Usually contains checkpoints and logs.
- **Videos**: 360-degree spins of the generated object.
- **Meshes**: If exported, `.obj` files representing the structure.

## 5. Troubleshooting Common Issues

- **OOM (Out of Memory)**: If your GPU runs out of memory, try reducing the batch size or the rendering resolution if the script exposes those arguments.
- **CUDA Errors**: Ensure `tiny-cuda-nn` was compiled with the same CUDA version as your PyTorch installation.
