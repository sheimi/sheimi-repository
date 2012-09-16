#include "histogram.h"
#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>
#include <opencv2/opencv.hpp>
#include <unistd.h>
#include <string>
#include <iostream>

using namespace cv;
using namespace std;

void extract_histogram(string& filename) {
  Mat image = imread(filename);
  Mat hsv;
  cvtColor(image, hsv, CV_BGR2HSV);
  
  int hbins = 8;
  int sbins = 4;
  int vbins = 4;
  int hist_size[] = {hbins, sbins, vbins}; // {hbins, sbins, vbins}
  float hrange[] = {0, 180};
  float srange[] = {0, 256};
  float vrange[] = {0, 256};
  const float* ranges[] = {hrange, srange, vrange};
  MatND hist;
  int channels[] = {0, 1, 2};
  calcHist(&hsv, 1, channels, Mat(),
           hist, 3, hist_size, ranges,
           true, false);
  for(int h = 0; h < hbins; h++)
    for(int s = 0; s < sbins; s++ )
      for(int v = 0; v < vbins; v++ ) {
        float bin_val = hist.at<float>(h, s, v);
        cout << bin_val << " ";
      }
  cout << endl;
}

int main(int argc, char** argv) {

  // get the param
  string src_dir_path = argv[1];

  // walk the dir
  DIR* src_dir = opendir(src_dir_path.c_str());
  struct dirent * dir;
  struct stat status;
  if (src_dir) {
    while ((dir = readdir(src_dir)) != NULL) {
      if (IS_EQUAL(dir->d_name, ".") || IS_EQUAL(dir->d_name, ".."))
        continue;
      if (S_ISDIR(status.st_mode)) 
        continue;
      if (dir->d_name[0] == '.')
        continue;
      string path = src_dir_path + '/' + dir->d_name;
      stat(path.c_str(), &status); 
      extract_histogram(path);
    }
    closedir(src_dir);
  }

}
