using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;

namespace dumpBCF
{
    class Program
    {
        static void Main(string[] args)
        {
            string myFile = @"C:\Windows\AppCompat\Programs\RecentFileCache.bcf";

            if(args.Length>0 && !File.Exists(args[0])){
                Console.WriteLine(@"usage: dumpBCF.exe myBCF.bcf" );
                Console.WriteLine(@"default file: "+myFile);
                Environment.Exit(0);
            }

            // 1.
            // Open as binary file.
            using (BinaryReader b = new BinaryReader(File.Open(myFile,
                                                               FileMode.Open)))
            {
                // 2.
                // Important variables:
                int length = (int)b.BaseStream.Length;
                int pos = 0x14;                

                // 3.
                // Seek the required index.
                b.BaseStream.Seek(pos, SeekOrigin.Begin);

                byte[] mySepBytes = new byte[] { 0x00,0x00};
                string mySepString = System.Text.Encoding.UTF8.GetString(mySepBytes).TrimEnd('\0');

                // 4.
                // Slow loop through the bytes.
                while (pos < length )
                {                    
                    int myLenth = b.ReadInt32()+1;
                    byte[] myBytes = b.ReadBytes(myLenth*2);
                    
                    // 5.
                    // Increment the variables.
                    string result = System.Text.Encoding.Unicode.GetString(myBytes).TrimEnd('\0');
                    Console.WriteLine(result);                    
                    pos += 4 + myLenth*2;
                }                
            }
        }
    }
}
