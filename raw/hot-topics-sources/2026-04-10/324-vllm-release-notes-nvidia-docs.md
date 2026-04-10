---
title: vLLM Release Notes - NVIDIA Docs
source_url: https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html
final_url: https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html
status: 200
content_type: text/html;charset=UTF-8
topics: [vLLM V1 Engine on Blackwell (GB200/GB300)]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:07.874221+00:00
---

# vLLM Release Notes - NVIDIA Docs

## 원본 URL

https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html

## 추출 본문

vLLM Release Notes - NVIDIA Docs

Topics

Topics

AR / VR

Cybersecurity

Edge Computing

Recommenders / Personalization

Computer Vision / Video Analytics

Data Center / Cloud

Generative AI / LLMs

Robotics

Content Creation / Rendering

Data Science

Networking

Simulation / Modeling / Design

Conversational AI

NVIDIA Developer

Blog

Forums

Sign In

Menu

Docs Hub

Topics

Topics

AR / VR

Cybersecurity

Edge Computing

Recommenders / Personalization

Computer Vision / Video Analytics

Data Center / Cloud

Generative AI / LLMs

Robotics

Content Creation / Rendering

Data Science

Networking

Simulation / Modeling / Design

Conversational AI

NVIDIA Developer

Blog

Forums

Sign In

NVIDIA Optimized Frameworks
Submit Search

Submit Search

NVIDIA Docs Hub HomepageNVIDIA Optimized FrameworksNVIDIA Optimized FrameworksvLLM Release Notes

Download PDF

vLLM Release Notes

vLLM Release Notes

 
 These release notes describe the key features, software enhancements, improvements, and known issues for this release of vLLM. vLLM is a high-performance serving engine for Large Language Models (LLMs) that provides state-of-the-art throughput and memory efficiency. The framework seamlessly integrates with the Python ecosystem and supports a wide array of models from hubs like Hugging Face.

Through core innovations like PagedAttention and continuous batching, vLLM is designed to be powerful and efficient for the most demanding inference workloads. Common use cases include powering generative AI applications, chatbots, and APIs for text generation, summarization, and translation. The vLLM container is released monthly to provide you with the latest NVIDIA deep learning software libraries and GitHub code contributions that have been sent upstream. The libraries and contributions have all been tested, tuned, and optimized.
 

Note:

Security Common Vulnerabilities and Exposures (CVEs)

Please review the Security Scanning tab on NGC to see the latest security scan results. For certain open-source vulnerabilities listed in the scan results, NVIDIA provides a response in the form of a Vulnerability Exploitability eXchange (VEX) document. The VEX information can be reviewed and downloaded from the Security Scanning tab.
 

For a complete view of the supported software and specific versions that are packaged with the frameworks based on the container image, see the Frameworks Support Matrix.
 

 
 
 Table of Contents
 
 

1. vLLM Overview

2. Pulling A Container

3. Running vLLM

4. vLLM Release 26.02

5. vLLM Release 26.01

6. vLLM Release 25.12

7. vLLM Release 25.11

8. vLLM Release 25.10

9. vLLM Release 25.09

© Copyright 2026, NVIDIA.Last updated on Mar 31, 2026

Topics

NVIDIA Optimized Frameworks

NVIDIA Optimized Frameworks

Preparing To Use Docker Containers

1. Introduction To Docker And Containers

2. Preparing Your DGX System For Use With NVIDIA Container Runtime

2.1. Version 2.x Or Earlier: Installing Docker And nvidia-docker2

2.2. Preventing IP Address Conflicts With Docker

2.2.1. Version 3.1.1 And Later: Preventing IP Address Conflicts Between Docker And DGX

2.2.2. Version 2.x Or Earlier: Preventing IP Address Conflicts Between Docker And DGX

2.3. Configuring The Use Of Proxies

2.4. Enabling Users To Run Docker Containers

3. Preparing To Use The Container Registry

Containers For Deep Learning Frameworks User Guide

1. Docker Containers

1.1. What Is A Docker Container?

1.2. Why Use A Container?

1.3. Hello World For Containers

1.4. Logging Into Docker

1.5. Listing Docker Images

2. Installing Docker And NVIDIA Container Runtime

2.1. Docker Best Practices

2.2. docker exec

2.3. nvcr.io

2.4. Building Containers

2.5. Using And Mounting File Systems

3. Pulling A Container

3.1. Key Concepts

3.2. Accessing And Pulling From The NGC container registry

3.2.1. Pulling A Container From The NGC container registry Using The Docker CLI

3.2.2. Pulling A Container Using The NGC Web Interface

3.3. Verifying

4. NGC Images

4.1. NGC Images Versions

5. Running A Container

5.1. Enabling GPU Support For NGC Containers

5.2. Example: Running A Container

5.3. Specifying A User

5.4. Setting The Remove Flag

5.5. Setting The Interactive Flag

5.6. Setting The Volumes Flag

5.7. Setting The Mapping Ports Flag

5.8. Setting The Shared Memory Flag

5.9. Setting The Restricting Exposure Of GPUs Flag

5.10. Container Lifetime

6. NVIDIA Deep Learning Software Stack

6.1. OS Layer

6.2. CUDA Layer

6.2.1. CUDA Runtime

6.2.2. CUDA Toolkit

6.3. Deep Learning Libraries Layer

6.3.1. NCCL

6.3.2. cuDNN Layer

6.4. Framework Containers

7. NVIDIA Deep Learning Framework Containers

7.1. Why Use a Deep Learning Software Framework?

7.2. Kaldi

7.3. TensorFlow

7.3.1. Running The TensorFlow Container

7.4. PyTorch

8. Frameworks General Best Practices

8.1. Extending Containers

8.2. Datasets And Containers

8.3. Working With Containerized VNC Desktop Environment

9. HPC And HPC Visualization Containers

10. Customizing And Extending Containers And Frameworks

10.1. Customizing A Container

10.1.1. Benefits And Limitations To Customizing A Container

10.1.2. Example 1: Building A Container From Scratch

10.1.3. Example 2: Customizing A Container Using Dockerfile

10.1.4. Example 3: Customizing A Container Using docker commit

10.1.5. Example 4: Developing A Container Using Docker

10.1.5.1. Example 4.1: Package The Source Into The Container

10.2. Customizing a Framework

10.2.1. Benefits and Limitations to Customizing a Framework

10.2.2. Example 1: Customizing A Framework Using The Command Line

10.2.3. Example 2: Customizing A Framework And Rebuilding The Container

10.3. Optimizing Docker Containers For Size

10.3.1. One Line Per RUN Command

10.3.2. Export, Import, And Flatten

10.3.3. docker-squash

10.3.4. Squash While Building

10.3.5. Additional Options

11. Scripts

11.1. TensorFlow

11.1.1. run_tf_cifar10.sh

11.2. Keras

11.2.1. cifar10_cnn_filesystem.py

12. Troubleshooting

Support Matrix

Frameworks Support Matrix

1. 26.xx Framework Containers Support Matrix

2. 25.xx Framework Containers Support Matrix

3. 24.xx Framework Containers Support Matrix

4. 23.xx Framework Containers Support Matrix

5. 22.xx Framework Containers Support Matrix

6. 21.xx Framework Containers Support Matrix

7. 20.xx Framework Containers Support Matrix

8. 19.xx Framework Containers Support Matrix

9. 18.xx Framework Containers Support Matrix

10. 17.xx Framework Containers Support Matrix

11. 16.xx Framework Containers Support Matrix

Optimized Frameworks Release Notes

CUDA DL Release Notes

1. CUDA DL Overview

2. Pulling A Container

3. Running CUDA DL

4. CUDA DL Release 26.03

5. CUDA DL Release 26.02

6. CUDA DL Release 26.01

7. CUDA DL Release 25.12

8. CUDA DL Release 25.11

9. CUDA DL Release 25.10

10. CUDA DL Release 25.09

11. CUDA DL Release 25.08

12. CUDA DL Release 25.06

13. CUDA DL Release 25.05

14. CUDA DL Release 25.04

15. CUDA DL Release 25.03

16. CUDA DL Release 25.02

TensorRT Release Notes

1. TensorRT Overview

2. Pulling A Container

3. Running TensorRT

4. TensorRT Release 26.03

5. TensorRT Release 26.02

6. TensorRT Release 26.01

7. TensorRT Release 25.12

8. TensorRT Release 25.11

9. TensorRT Release 25.10

10. TensorRT Release 25.09

11. TensorRT Release 25.08

12. TensorRT Release 25.06

13. TensorRT Release 25.05

14. TensorRT Release 25.04

15. TensorRT Release 25.03

16. TensorRT Release 25.02

17. TensorRT Release 25.01

18. TensorRT Release 24.12

19. TensorRT Release 24.11

20. TensorRT Release 24.10

21. TensorRT Release 24.09

22. TensorRT Release 24.08

23. TensorRT Release 24.07

24. TensorRT Release 24.06

25. TensorRT Release 24.05

26. TensorRT Release 24.04

27. TensorRT Release 24.03

28. TensorRT Release 24.02

29. TensorRT Release 24.01

30. TensorRT Release 23.12

31. TensorRT Release 23.11

32. TensorRT Release 23.10

33. TensorRT Release 23.09

34. TensorRT Release 23.08

35. TensorRT Release 23.07

36. TensorRT Release 23.06

37. TensorRT Release 23.05

38. TensorRT Release 23.04

39. TensorRT Release 23.03

40. TensorRT Release 23.02

41. TensorRT Release 23.01

42. TensorRT Release 22.12

43. TensorRT Release 22.11

44. TensorRT Release 22.10

45. TensorRT Release 22.09

46. TensorRT Release 22.08

47. TensorRT Release 22.07

48. TensorRT Release 22.06

49. TensorRT Release 22.05

50. TensorRT Release 22.04

51. TensorRT Release 22.03

52. TensorRT Release 22.02

53. TensorRT Release 22.01

54. TensorRT Release 21.12

55. TensorRT Release 21.11

56. TensorRT Release 21.10

57. TensorRT Release 21.09

58. TensorRT Release 21.08

59. TensorRT Release 21.07

60. TensorRT Release 21.06

61. TensorRT Release 21.05

62. TensorRT Release 21.04

63. TensorRT Release 21.03

64. TensorRT Release 21.02

65. TensorRT Release 21.01

66. TensorRT Release 20.12

67. TensorRT Release 20.11

68. TensorRT Release 20.10

69. TensorRT Release 20.09

70. TensorRT Release 20.08

71. TensorRT Release 20.07

72. TensorRT Release 20.06

73. TensorRT Release 20.03

74. TensorRT Release 20.02

75. TensorRT Release 20.01

76. TensorRT Release 19.12

77. TensorRT Release 19.11

78. TensorRT Release 19.10

79. TensorRT Release 19.09

80. TensorRT Release 19.08

81. TensorRT Release 19.07

82. TensorRT Release 19.06

83. TensorRT Release 19.05

84. TensorRT Release 19.04

85. TensorRT Release 19.03

86. TensorRT Release 19.02

87. TensorRT Release 19.01

88. TensorRT Release 18.12

89. TensorRT Release 18.11

90. TensorRT Release 18.10

91. TensorRT Release 18.09

92. TensorRT Release 18.08

93. TensorRT Release 18.07

94. TensorRT Release 18.06

95. TensorRT Release 18.05

96. TensorRT Release 18.04

97. TensorRT Release 18.03

98. TensorRT Release 18.02

99. TensorRT Release 18.01

100. TensorRT Release 17.12

DGL Release Notes

1. DGL Overview

2. Pulling A Container

3. Running DGL

4. DGL Release 25.10

5. DGL Release 25.09

6. DGL Release 25.08

7. DGL Release 25.06

8. DGL Release 25.05

9. DGL Release 25.04

10. DGL Release 25.03

11. DGL Release 25.02

12. DGL Release 25.01

13. DGL Release 24.12

14. DGL Release 24.11

15. DGL Release 24.10

16. DGL Release 24.09

17. DGL Release 24.08

18. DGL Release 24.07

19. DGL Release 24.06

20. DGL Release 24.05

21. DGL Release 24.04

22. DGL Release 24.03

23. DGL Release 24.02

24. DGL Release 24.01

25. DGL Release 23.12

26. DGL Release 23.11

27. DGL Release 23.09

28. DGL Release 23.07

JAX Release Notes

1. JAX Overview

2. Pulling A Container

3. Running JAX

4. JAX Release 26.03

5. JAX Release 26.02

6. JAX Release 26.01

7. JAX Release 25.12

8. JAX Release 25.11

9. JAX Release 25.10

10. JAX Release 25.09

11. JAX Release 25.08

12. JAX Release 25.06

13. JAX Release 25.05

14. JAX Release 25.04

15. JAX Release 25.03

16. JAX Release 25.02

17. JAX Release 25.01

18. JAX Release 24.12

19. JAX Release 24.11

20. JAX Release 24.10

21. JAX Release 24.09

22. JAX Release 24.08

23. JAX Release 24.07

24. JAX Release 24.06

25. JAX Release 24.05

26. JAX Release 24.04

27. JAX Release 24.03

28. JAX Release 24.02

29. JAX Release 23.12

30. JAX Release 23.10

31. JAX Release 23.08

Kaldi Release Notes

1. Kaldi Overview

2. Pulling A Container

3. Running Kaldi

4. Kaldi Release 24.02

5. Kaldi Release 24.01

6. Kaldi Release 23.12

7. Kaldi Release 23.11

8. Kaldi Release 23.10

9. Kaldi Release 23.09

10. Kaldi Release 23.08

11. Kaldi Release 23.07

12. Kaldi Release 23.06

13. Kaldi Release 23.05

14. Kaldi Release 23.04

15. Kaldi Release 23.03

16. Kaldi Release 23.02

17. Kaldi Release 23.01

18. Kaldi Release 22.12

19. Kaldi Release 22.11

20. Kaldi Release 22.10

21. Kaldi Release 22.09

22. Kaldi Release 22.08

23. Kaldi Release 22.07

24. Kaldi Release 22.06

25. Kaldi Release 22.05

26. Kaldi Release 22.04

27. Kaldi Release 22.03

28. Kaldi Release 22.02

29. Kaldi Release 22.01

30. Kaldi Release 21.12

31. Kaldi Release 21.11

32. Kaldi Release 21.10

33. Kaldi Release 21.09

34. Kaldi Release 21.08

35. Kaldi Release 21.07

36. Kaldi Release 21.06

37. Kaldi Release 21.05

38. Kaldi Release 21.04

39. Kaldi Release 21.03

40. Kaldi Release 21.02

41. Kaldi Release 21.01

42. Kaldi Release 20.12

43. Kaldi Release 20.11

44. Kaldi Release 20.10

45. Kaldi Release 20.09

46. Kaldi Release 20.08

47. Kaldi Release 20.07

48. Kaldi Release 20.06

49. Kaldi Release 20.03

50. Kaldi Release 20.02

51. Kaldi Release 20.01

52. Kaldi Release 19.12

53. Kaldi Release 19.11

54. Kaldi Release 19.10

55. Kaldi Release 19.09

56. Kaldi Release 19.08

57. Kaldi Release 19.07

58. Kaldi Release 19.06

59. Kaldi Release 19.05

60. Kaldi Release 19.04

61. Kaldi Release 19.03

NVIDIA Optimized Deep Learning Framework, powered by Apache MXNet Release Notes

1. Overview

2. Pulling A Container

3. Running NVIDIA Optimized Deep Learning Framework, powered by Apache MXNet

4. Release 24.11

5. Release 24.10

6. Release 24.09

7. Release 24.08

8. Release 24.07

9. Release 24.06

10. Release 24.05

11. Release 24.04

12. Release 24.03

13. Release 24.02

14. Release 24.01

15. Release 23.12

16. Release 23.11

17. Release 23.10

18. Release 23.09

19. Release 23.08

20. Release 23.07

21. Release 23.06

22. Release 23.05

23. Release 23.04

24. Release 23.03

25. Release 23.02

26. Release 23.01

27. Release 22.12

28. Release 22.11

29. Release 22.10

30. Release 22.09

31. Release 22.08

32. Release 22.07

33. Release 22.06

34. Release 22.05

35. Release 22.04

36. Release 22.03

37. Release 21.09

38. Release 21.08

39. Release 21.07

40. Release 21.06

41. Release 21.05

42. Release 21.04

43. Release 21.03

44. Release 21.02

45. Release 21.01

46. Release 20.12

47. Release 20.11

48. Release 20.10

49. Release 20.09

50. Release 20.08

51. Release 20.07

52. Release 20.06

53. Release 20.03

54. Release 20.02

55. Release 20.01

56. Release 19.12

57. Release 19.11

58. Release 19.10

59. Release 19.09

60. Release 19.08

61. Release 19.07

62. Release 19.06

63. Release 19.05

64. Release 19.04

65. Release 19.03

66. Release 19.02

67. Release 19.01

68. Release 18.12

69. Release 18.11

70. Release 18.10

71. Release 18.09

72. Release 18.08

73. Release 18.07

74. Release 18.06

75. Release 18.05

76. Release 18.04

77. Release 18.03

78. Release 18.02

79. Release 18.01

80. Release 17.12

81. Release 17.11

82. Release 17.10

83. Release 17.09

84. Release 17.07

85. Release 17.06

86. Release 17.05

87. Release 17.04

88. Release 17.03

PyTorch Release Notes

1. PyTorch Overview

2. Pulling A Container

3. Running PyTorch

4. PyTorch Release 26.03

5. PyTorch Release 26.02

6. PyTorch Release 26.01

7. PyTorch Release 25.12

8. PyTorch Release 25.11

9. PyTorch Release 25.10

10. PyTorch Release 25.09

11. PyTorch Release 25.08

12. PyTorch Release 25.06

13. PyTorch Release 25.05

14. PyTorch Release 25.04

15. PyTorch Release 25.03

16. PyTorch Release 25.02

17. PyTorch Release 25.01

18. PyTorch Release 24.12

19. PyTorch Release 24.11

20. PyTorch Release 24.10

21. PyTorch Release 24.09

22. PyTorch Release 24.08

23. PyTorch Release 24.07

24. PyTorch Release 24.06

25. PyTorch Release 24.05

26. PyTorch Release 24.04

27. PyTorch Release 24.03

28. PyTorch Release 24.02

29. PyTorch Release 24.01

30. PyTorch Release 23.12

31. PyTorch Release 23.11

32. PyTorch Release 23.10

33. PyTorch Release 23.09

34. PyTorch Release 23.08

35. PyTorch Release 23.07

36. PyTorch Release 23.06

37. PyTorch Release 23.05

38. PyTorch Release 23.04

39. PyTorch Release 23.03

40. PyTorch Release 23.02

41. PyTorch Release 23.01

42. PyTorch Release 22.12

43. PyTorch Release 22.11

44. PyTorch Release 22.10

45. PyTorch Release 22.09

46. PyTorch Release 22.08

47. PyTorch Release 22.07

48. PyTorch Release 22.06

49. PyTorch Release 22.05

50. PyTorch Release 22.04

51. PyTorch Release 22.03

52. PyTorch Release 22.02

53. PyTorch Release 22.01

54. PyTorch Release 21.12

55. PyTorch Release 21.11

56. PyTorch Release 21.10

57. PyTorch Release 21.09

58. PyTorch Release 21.08

59. PyTorch Release 21.07

60. PyTorch Release 21.06

61. PyTorch Release 21.05

62. PyTorch Release 21.04

63. PyTorch Release 21.03

64. PyTorch Release 21.02

65. PyTorch Release 21.01

66. PyTorch Release 20.12

67. PyTorch Release 20.11

68. PyTorch Release 20.10

69. PyTorch Release 20.09

70. PyTorch Release 20.08

71. PyTorch Release 20.07

72. PyTorch Release 20.06

73. PyTorch Release 20.03

74. PyTorch Release 20.02

75. PyTorch Release 20.01

76. PyTorch Release 19.12

77. PyTorch Release 19.11

78. PyTorch Release 19.10

79. PyTorch Release 19.09

80. PyTorch Release 19.08

81. PyTorch Release 19.07

82. PyTorch Release 19.06

83. PyTorch Release 19.05

84. PyTorch Release 19.04

85. PyTorch Release 19.03

86. PyTorch Release 19.02

87. PyTorch Release 19.01

88. PyTorch Release 18.12

89. PyTorch Release 18.11

90. PyTorch Release 18.10

91. PyTorch Release 18.09

92. PyTorch Release 18.08

93. PyTorch Release 18.07

94. PyTorch Release 18.06

95. PyTorch Release 18.05

96. PyTorch Release 18.04

97. PyTorch Release 18.03

98. PyTorch Release 18.02

99. PyTorch Release 18.01

100. PyTorch Release 17.12

101. PyTorch Release 17.11

102. PyTorch Release 17.10

103. PyTorch Release 17.09

104. PyTorch Release 17.07

105. PyTorch Release 17.06

106. PyTorch Release 17.05

107. PyTorch Release 17.04

PyG Release Notes

1. PyG Overview

2. Pulling A Container

3. Running PyG

4. PyG Release 26.03

5. PyG Release 26.02

6. PyG Release 26.01

7. PyG Release 25.12

8. PyG Release 26.01

9. PyG Release 25.10

10. PyG Release 25.09

11. PyG Release 25.08

12. PyG Release 25.06

13. PyG Release 25.05

14. PyG Release 25.04

15. PyG Release 25.03

16. PyG Release 25.02

17. PyG Release 25.01

18. PyG Release 24.12

19. PyG Release 24.11

20. PyG Release 24.10

21. PyG Release 24.09

22. PyG Release 24.08

23. PyG Release 24.07

24. PyG Release 24.06

25. PyG Release 24.05

26. PyG Release 24.03

27. PyG Release 24.02

28. PyG Release 24.01

29. PyG Release 23.12

30. PyG Release 23.11

31. PyG Release 23.01

PaddlePaddle Release Notes

1. PaddlePaddle Overview

2. Pulling a Container

3. Running PaddlePaddle

4. PaddlePaddle Release 25.01

5. PaddlePaddle Release 24.12

6. PaddlePaddle Release 24.11

7. PaddlePaddle Release 24.10

8. PaddlePaddle Release 24.09

9. PaddlePaddle Release 24.08

10. PaddlePaddle Release 24.07

11. PaddlePaddle Release 24.06

12. PaddlePaddle Release 24.05

13. PaddlePaddle Release 24.04

14. PaddlePaddle Release 24.03

15. PaddlePaddle Release 24.02

16. PaddlePaddle Release 24.01

17. PaddlePaddle Release 23.12

18. PaddlePaddle Release 23.11

19. PaddlePaddle Release 23.10

20. PaddlePaddle Release 23.09

21. PaddlePaddle Release 23.08

22. PaddlePaddle Release 23.07

23. PaddlePaddle Release 23.06

24. PaddlePaddle Release 23.04

25. PaddlePaddle Release 23.03

26. PaddlePaddle Release 23.02

27. PaddlePaddle Release 23.01

28. PaddlePaddle Release 22.12

29. PaddlePaddle Release 22.11

30. PaddlePaddle Release 22.10

31. PaddlePaddle Release 22.09

32. PaddlePaddle Release 22.08

33. PaddlePaddle Release 22.07

34. PaddlePaddle Release 22.06

35. PaddlePaddle Release 22.05

SGLang Release Notes

1. SGLang Overview

2. Pulling A Container

3. Running SGLang

4. SGLang Release 26.02

5. SGLang Release 26.01

6. SGLang Release 25.12

7. SGLang Release 25.11

8. SGLang Release 25.10

TensorFlow Release Notes

1. TensorFlow Overview

2. Pulling A Container

3. Running TensorFlow

4. TensorFlow Release 25.02

5. TensorFlow Release 25.01

6. TensorFlow Release 24.12

7. TensorFlow Release 24.11

8. TensorFlow Release 24.10

9. TensorFlow Release 24.09

10. TensorFlow Release 24.08

11. TensorFlow Release 24.07

12. TensorFlow Release 24.06

13. TensorFlow Release 24.05

14. TensorFlow Release 24.04

15. TensorFlow Release 24.03

16. TensorFlow Release 24.02

17. TensorFlow Release 24.01

18. TensorFlow Release 23.12

19. TensorFlow Release 23.11

20. TensorFlow Release 23.10

21. TensorFlow Release 23.09

22. TensorFlow Release 23.08

23. TensorFlow Release 23.07

24. TensorFlow Release 23.06

25. TensorFlow Release 23.05

26. TensorFlow Release 23.04

27. TensorFlow Release 23.03

28. TensorFlow Release 23.02

29. TensorFlow Release 23.01

30. TensorFlow Release 22.12

31. TensorFlow Release 22.11

32. TensorFlow Release 22.10.1

33. TensorFlow Release 22.10

34. TensorFlow Release 22.09

35. TensorFlow Release 22.08

36. TensorFlow Release 22.07

37. TensorFlow Release 22.06

38. TensorFlow Release 22.05

39. TensorFlow Release 22.04

40. TensorFlow Release 22.03

41. TensorFlow Release 22.02

42. TensorFlow Release 22.01

43. TensorFlow Release 21.12

44. TensorFlow Release 21.11

45. TensorFlow Release 21.10

46. TensorFlow Release 21.09

47. TensorFlow Release 21.08

48. TensorFlow Release 21.07

49. TensorFlow Release 21.06

50. TensorFlow Release 21.05

51. TensorFlow Release 21.04

52. TensorFlow Release 21.03

53. TensorFlow Release 21.02

54. TensorFlow Release 21.01

55. TensorFlow Release 20.12

56. TensorFlow Release 20.11

57. TensorFlow Release 20.10

58. TensorFlow Release 20.09

59. TensorFlow Release 20.08

60. TensorFlow Release 20.07

61. TensorFlow Release 20.06

62. TensorFlow Release 20.03

63. TensorFlow Release 20.02

64. TensorFlow Release 20.01

65. TensorFlow Release 19.12

66. TensorFlow Release 19.11

67. TensorFlow Release 19.10

68. TensorFlow Release 19.09

69. TensorFlow Release 19.08

70. TensorFlow Release 19.07

71. TensorFlow Release 19.06

72. TensorFlow Release 19.05

73. TensorFlow Release 19.04

74. TensorFlow Release 19.03

75. TensorFlow Release 19.02

76. TensorFlow Release 19.01

77. TensorFlow Release 18.12

78. TensorFlow Release 18.11

79. TensorFlow Release 18.10

80. TensorFlow Release 18.09

81. TensorFlow Release 18.08

82. TensorFlow Release 18.07

83. TensorFlow Release 18.06

84. TensorFlow Release 18.05

85. TensorFlow Release 18.04

86. TensorFlow Release 18.03

87. TensorFlow Release 18.02

88. TensorFlow Release 18.01

89. TensorFlow Release 17.12

90. TensorFlow Release 17.11

91. TensorFlow Release 17.10

92. TensorFlow Release 17.09

93. TensorFlow Release 17.07

94. TensorFlow Release 17.06

95. TensorFlow Release 17.05

96. TensorFlow Release 17.04

97. TensorFlow Release 17.03

98. TensorFlow Release 17.02

99. TensorFlow Release 17.01

100. TensorFlow Release 16.12

TensorFlow Wheel Release Notes

1. Overview

2. TensorFlow Wheel Platform

2.1. TensorFlow Wheel Release 23.03

2.2. TensorFlow Wheel Release 23.02

2.3. TensorFlow Wheel Release 23.01

2.4. TensorFlow Wheel Release 22.12

2.5. TensorFlow Wheel Release 22.11

2.6. TensorFlow Wheel Release 22.10

2.7. TensorFlow Wheel Release 22.09

2.8. TensorFlow Wheel Release 22.08

2.9. TensorFlow Wheel Release 22.07

2.10. TensorFlow Wheel Release 22.06

2.11. TensorFlow Wheel Release 22.05

2.12. TensorFlow Wheel Release 22.04

2.13. TensorFlow Wheel Release 22.03

2.14. TensorFlow Wheel Release 22.02

2.15. TensorFlow Wheel Release 22.01

2.16. TensorFlow Wheel Release 21.12

2.17. TensorFlow Wheel Release 21.11

2.18. TensorFlow Wheel Release 21.10

2.19. TensorFlow Wheel Release 21.09

2.20. TensorFlow Wheel Release 21.08

2.21. TensorFlow Wheel Release 21.07

2.22. TensorFlow Wheel Release 21.06

2.23. TensorFlow Wheel Release 21.05

2.24. TensorFlow Wheel Release 21.04

2.25. TensorFlow Wheel Release 21.03

2.26. TensorFlow Wheel Release 21.02

2.27. TensorFlow Wheel Release 21.01

2.28. TensorFlow Wheel Release 20.12

2.29. TensorFlow Wheel Release 20.11

2.30. TensorFlow Wheel Release 20.10

2.31. TensorFlow Wheel Release 20.09

2.32. TensorFlow Wheel Release 20.08

2.33. TensorFlow Wheel Release 20.07

2.34. TensorFlow Wheel Release 20.06

vLLM Release Notes

1. vLLM Overview

2. Pulling A Container

3. Running vLLM

4. vLLM Release 26.02

5. vLLM Release 26.01

6. vLLM Release 25.12

7. vLLM Release 25.11

8. vLLM Release 25.10

9. vLLM Release 25.09

Optimized Frameworks User Guides

TensorFlow User Guide

1. Overview Of TensorFlow

1.1. Contents Of The NVIDIA TensorFlow Container

2. Pulling The TensorFlow Container

3. Running A TensorFlow Container

4. Verifying TensorFlow

5. Customizing And Extending TensorFlow

5.1. Benefits And Limitations To Customizing TensorFlow

5.2. Example 1: Customizing TensorFlow Using Dockerfile

5.3. Example 2: Customizing TensorFlow Using docker commit

5.4. Accelerating Inference In TensorFlow With TensorRT

6. TensorFlowParameters

6.1. Added And Modified Parameters

6.1.1. TF_CUDA_COMPUTE_CAPABILITIES

6.1.2. TF_NEED_GCP

6.1.3. TF_NEED_HDFS

6.1.4. TF_ENABLE_XLA

7. TensorFlow Environment Variables

7.1. Added Or Modified Variables

7.1.1. TF_ADJUST_HUE_FUSED

7.1.2. TF_ADJUST_SATURATION_FUSED

7.1.3. TF_ENABLE_WINOGRAD_NONFUSED

7.1.4. TF_AUTOTUNE_THRESHOLD

7.1.5. CUDA_DEVICE_MAX_CONNECTIONS

7.1.6. TF_DISABLE_CUDNN_TENSOR_OP_MATH

7.1.7. TF_DISABLE_CUDNN_RNN_TENSOR_OP_MATH

7.1.8. TF_DISABLE_CUBLAS_TENSOR_OP_MATH

7.1.9. TF_ENABLE_CUBLAS_TENSOR_OP_MATH_FP32

7.1.10. TF_ENABLE_CUDNN_TENSOR_OP_MATH_FP32

7.1.11. TF_ENABLE_CUDNN_RNN_TENSOR_OP_MATH_FP32

7.1.12. TF_ENABLE_LAYOUT_NHWC

7.1.13. TF_ENABLE_NVTX_RANGES

7.1.14. TF_CUDNN_CTC_LOSS

7.1.15. TF_GPU_ALLOCATOR

7.1.16. TF_GRAPPLER_GRAPH_DEF_PATH

8. Performance

8.1. Tensor Core Math

8.1.1. Float16 Training

8.2. Automatic Mixed Precision (AMP)

8.2.1. Automatic Mixed Precision Training In TensorFlow

8.2.2. Conditions And Limitations

8.2.3. FAQs

9. XLA Best Practices

9.1. XLA Introduction

9.1.1. Why Use XLA?

9.1.2. Enabling XLA

9.1.2.1. XLA Lite

9.1.3. XLA Caveats

9.2. TF-XLA Integration

9.2.1. Changes to the TensorFlow Graph

9.2.1.1. Clustering

9.2.1.2. TensorFlow Graph Execution with XLA

9.2.2. Symptoms of XLA Issues

9.2.2.1. Functional Issues

9.2.2.2. Performance Issues

9.3. Identifying and Managing the Issues

9.3.1. Controlling XLA with Environment Variables

9.3.2. Out of Memory Issue

9.3.2.1. Memory Fragmentation

9.3.3. TensorFlow-XLA Performance Issues

9.3.3.1. TensorFlow-XLA Integration Issues

9.3.3.2. Compilation Overhead

9.3.3.3. Compute/Communication Overlap

9.3.4. XLA Optimizer and Code Generation

9.3.4.1. XLA Autotune

9.3.4.2. Various Options

9.4. XLA Options Reference

10. Troubleshooting

10.1. Support

Installing Frameworks for Jetson

Installing TensorFlow for Jetson Platform

1. Overview

1.1. Benefits of TensorFlow on Jetson Platform

2. Prerequisites and Dependencies

3. Installing TensorFlow

3.1. Installing Multiple TensorFlow Versions

3.2. Upgrading TensorFlow

4. Verifying The Installation

5. Best Practices

6. Uninstalling

7. Troubleshooting

8. Support

TensorFlow for Jetson Platform Release Notes

1. Overview

2. TensorFlow on Jetson Platform

Installing PyTorch for Jetson Platform

1. Overview

1.1. Benefits of PyTorch for Jetson Platform

2. Prerequisites and Installation

2.1. Installing Multiple PyTorch Versions

2.2. Upgrading PyTorch

3. Verifying The Installation

4. Uninstalling

5. Troubleshooting

PyTorch for Jetson Platform Release Notes

1. Overview

2. PyTorch for Jetson Platform

Accelerating Inference In Frameworks With TensorRT

Accelerating Inference in TensorFlow with TensorRT User Guide

1. Introduction

2. Downloading and Installing TF-TRT

3. Quickstart Guide

4. Key Capabilities

4.1. Supported Precision Levels

4.2. Quantization

4.2.1. Post-Training Quantization

4.3. Dynamic Shapes

4.4. Simple Examples

4.4.1. A Python Example

4.4.2. A C++ Example

5. Deploying TF-TRT

6. Debugging and Troubleshooting

6.1. Minimum Segment Size

6.2. Max Workspace Size

6.3. Conversion Reports

6.3.1. converter.summary()

6.3.2. Conversion Report

6.4. Logging

6.5. Export TRT Engines for Debugging

6.6. Blocking Conversion of Ops for Debugging

6.7. Using Experimental Features

6.8. Overriding top_k Threshold for the NMS Plugin

6.9. Enabling the Tensor Layout Optimizer

6.10. Allowing Fallback to TF Native Segment Execution

6.11. Controlling the Number of Engines Generated

6.12. Visualizing the TF-TRT Graph

7. Best Practices

8. Advanced Features

8.1. Memory Management

8.2. Max Cached Engines

Corporate Info

NVIDIA.com Home

About NVIDIA

‎NVIDIA Developer

Developer Home

Blog

Resources

Contact Us

Developer Program

Privacy Policy | Your Privacy Choices | Terms of Service | Accessibility | Corporate Policies | Product Security | Contact

Copyright © 2026 NVIDIA Corporation

Close

 content here
