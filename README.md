# AES Image Encryption & Decryption

A cryptography project developed for **COMP453 – Cryptography** at **MEF University**.

This project explores how the **Advanced Encryption Standard (AES)** behaves when applied to digital images using three block cipher modes:

- **ECB (Electronic Codebook)**
- **CBC (Cipher Block Chaining)**
- **CTR (Counter Mode)**

The project compares the modes in terms of **visual information leakage, encryption/decryption performance, and reconstruction quality**.

---

## Project Overview

Digital images contain large regions of spatial correlation, repeated textures, and recurring color patterns. Although AES itself is cryptographically secure, the selected mode of operation can strongly affect whether visual structure remains visible in encrypted image data.

This project:

- Converts image files into an uncompressed RGB BMP representation
- Extracts raw pixel bytes
- Encrypts the image using AES-ECB, AES-CBC, and AES-CTR
- Reconstructs encrypted images for visual comparison
- Decrypts each encrypted output
- Measures encryption and decryption time
- Computes PSNR to verify reconstruction quality
- Generates comparison plots for technical analysis

---

## AES Modes Compared

### ECB — Electronic Codebook

ECB encrypts every block independently.

**Characteristics**
- Identical plaintext blocks produce identical ciphertext blocks
- Fast and simple
- Preserves visible structural patterns in image data
- Not suitable for protecting images with repeated visual content

The experiment clearly demonstrates **pattern leakage** in the encrypted ECB image.

---

### CBC — Cipher Block Chaining

CBC chains blocks together using an initialization vector (IV).

**Characteristics**
- Each block depends on the previous ciphertext block
- Repeated plaintext blocks do not produce repeated ciphertext blocks
- Removes visible structural patterns
- Sequential dependency makes it less parallelizable than CTR

CBC successfully hides the original image structure in the experiment.

---

### CTR — Counter Mode

CTR converts AES into a stream-like cipher by encrypting successive counter values and XORing the result with plaintext.

**Characteristics**
- Supports parallel processing
- Does not require padding
- Removes visible image patterns
- Provides strong performance for multimedia-style data

In the project experiments, CTR provided strong security properties together with competitive execution speed.

---

## Methodology

The project follows this pipeline:

```text
Input Image
    ↓
Convert JPG → RGB BMP
    ↓
Extract Raw Pixel Bytes
    ↓
AES Encryption
 ┌─────┬─────┬─────┐
 │ ECB │ CBC │ CTR │
 └─────┴─────┴─────┘
    ↓
Reconstruct Encrypted Images
    ↓
Decrypt
    ↓
Compare with Original
    ↓
Measure Runtime + PSNR
    ↓
Generate Result Graphs
```

---

## Results

### Visual Security

The encrypted outputs demonstrate a major difference between modes:

| AES Mode | Visual Pattern Leakage | Parallelizable | General Observation |
|---|---|---|---|
| ECB | High | Yes | Original structure remains partially visible |
| CBC | Very Low | No | Strong diffusion removes visible structure |
| CTR | Very Low | Yes | Strong diffusion with efficient processing |

### Reconstruction Quality

All three modes successfully reconstructed the original image after decryption.

| Mode | PSNR |
|---|---:|
| ECB | 100 dB |
| CBC | 100 dB |
| CTR | 100 dB |

A PSNR value of **100 dB** in this implementation indicates effectively lossless reconstruction.

### Performance Analysis

The project measures both encryption and decryption execution time for each AES mode and generates comparison plots.

The report's experimental analysis highlights:

- ECB is fast but visually insecure for structured image data
- CBC hides image structure effectively but introduces sequential dependency
- CTR combines strong visual protection with parallelizable operation

---

## Project Structure

```text
aes-image-encryption/
│
├── main3.py
├── create_bmp.py
├── input.bmp
├── input2.jpg
│
├── graphs/
│   ├── time_line_plot.png
│   ├── psnr_line_plot.png
│   ├── encrypted_comparison_line_version.png
│   └── aes_comparison_figure.png
│
├── docs/
│   └── COMP453_AES_Image_Encryption_Report.pdf
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies

- **Python**
- **PyCryptodome**
- **Pillow**
- **NumPy**
- **Matplotlib**
- **AES**
- **ECB / CBC / CTR**
- Image Processing
- Cryptographic Performance Analysis

---

## Installation

Clone the repository:

```bash
git clone https://github.com/erkisiel/aes-image-encryption.git
cd aes-image-encryption
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

To prepare the BMP image:

```bash
python create_bmp.py
```

Run the AES comparison:

```bash
python main3.py
```

The program generates:

- AES encrypted images
- AES decrypted images
- Performance graphs
- PSNR comparison plots
- Multi-mode visual comparisons

---

## Main Implementation

The project implements dedicated functions for each AES mode:

```python
aes_encrypt_ecb(...)
aes_decrypt_ecb(...)

aes_encrypt_cbc(...)
aes_decrypt_cbc(...)

aes_encrypt_ctr(...)
aes_decrypt_ctr(...)
```

The implementation also measures runtime and verifies decrypted output quality using PSNR.

---

## Key Takeaways

This project demonstrates that selecting the correct **mode of operation** is just as important as selecting a secure encryption algorithm.

The main experimental observations are:

- **ECB should not be used for structured visual data** because repeated plaintext blocks can reveal image patterns.
- **CBC provides strong diffusion** and removes visible image structure.
- **CTR provides strong confidentiality while supporting parallel processing.**
- Correct AES decryption reconstructs the original image without loss in the tested pipeline.

---

## Full Project Report

The detailed academic report contains:

- AES mode explanations
- Source code discussion
- Encrypted/decrypted output comparisons
- Performance measurements
- PSNR analysis
- Experimental results
- Technical discussion
- Full source-code appendix

[View the full COMP453 project report](docs/COMP453_AES_Image_Encryption_Report.pdf)

---

## Academic Context

**Course:** COMP453 – Cryptography  
**University:** MEF University  
**Department:** Computer Engineering  
**Student:** Elif Erkişi  
**Instructor:** Asst. Prof. Funda Özdemir  
**Project:** AES Image Encryption/Decryption in ECB, CBC, and CTR Modes

---

## Author

**Elif Erkişi**  
Computer Engineering  
MEF University
