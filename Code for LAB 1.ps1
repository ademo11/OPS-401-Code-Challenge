# LockScreen.ps1

Add-Type -TypeDefinition @"
    using System;
    using System.Runtime.InteropServices;

    public class LockWorkStation {
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool LockWorkStation();
    }
"@

# Call the LockWorkStation method to lock the screen
[LockWorkStation]::LockWorkStation()

# Reference
## OpenAI
