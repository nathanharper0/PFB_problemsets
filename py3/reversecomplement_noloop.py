#!/usr/bin/env python3
dna = 'AAAacCGGAtTgcGC'
#dna = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT'
dna_upper=dna.upper()
dna_rev=dna_upper[::-1]
dna_revcomp=dna_rev
dna_revcomp1=dna_revcomp.replace("G","c")
dna_revcomp2=dna_revcomp1.replace("C","g")
dna_revcomp3=dna_revcomp2.replace("A","t")
dna_revcomp4=dna_revcomp3.replace("T","a")
dna_reversecomplement=dna_revcomp4.upper()


print(f"{'Original Sequence':<20} 5\' {dna_upper} 3\'")
print(f"{'Complement':<20} 3\' {dna_rev} 3\'")
print(f"{'Reverse Complement':<20} 5\' {dna_reversecomplement} 3\'")
