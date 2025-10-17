import kagglehub

# Download latest version
path = kagglehub.dataset_download("kanakbaghel/hospital-management-dataset")

print("Path to dataset files:", path)