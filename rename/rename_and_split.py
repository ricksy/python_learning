# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():
    i = 0
    indir="/home/a/dev/data/tesla_model_x/"
    outdir="/home/a/dev/data/x/"
    if not os.path.exists(outdir):
    	os.makedirs(outdir)
    if not os.path.exists(outdir+ "train/"):
    	os.makedirs(outdir+ "train/")
    if not os.path.exists(outdir+ "vaild/"):
    	os.makedirs(outdir+ "valid/")

    for filename in os.listdir(indir):
        if (i % 2) == 0:
            dst = outdir + "train/" + str(i) + ".jpg"
        else:
            dst = outdir + "valid/" + str(i) + ".jpg"
        src = indir+ filename
	    # rename() function will
	    # rename all the files
        os.rename(src, dst)
        i += 1

# Driver Code
if __name__ == '__main__':

	# Calling main() function
    main()


