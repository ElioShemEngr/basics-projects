// Returns a random DNA base
const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G']
    return dnaBases[Math.floor(Math.random() * 4)] 
  }
  
  // Returns a random single strand of DNA containing 15 bases
  const mockUpStrand = () => {
    const newStrand = []
    for (let i = 0; i < 15; i++) {
      newStrand.push(returnRandBase())
    }
    return newStrand
  }
  
  
const pAequorFactory = (number, array) => {
    return {
        specimenNum: number,
        dna: array,
        mutate() {
            const randomIndex = Math.floor(Math.random() * this.dna.length);
            let newBase = returnRandBase();
            while (this.dna[randomIndex] === newBase) {
                newBase = returnRandBase();
            }
            this.dna[randomIndex] = newBase;
            return this.dna;
        },
        compareDNA(pAequor) {
            let count = 0;
            for (let i = 0; i < this.dna.length; i++) {
                if (this.dna[i] === pAequor.dna[i]) {
                    count++;
                }
            }
            const percentage = (count / this.dna.length) * 100;
            console.log(`Specimen #${this.specimenNum} and specimen #${pAequor.specimenNum} have ${percentage.toFixed(2)}% DNA in common.`);
        },
        willLikelySurvive() {
            const cOrG = this.dna.filter(el => el === 'C' || el === 'G');
            return cOrG.length / this.dna.length >= 0.6;
        },
        complementStrand() {
            return this.dna.map(el => {
                switch (el) {
                    case 'A':
                        return 'T';
                    case 'T':
                        return 'A';
                    case 'C':
                        return 'G';
                    case 'G':
                        return 'C';
                }
            });
        }
    }
}

const pAequorInstances = [];

let i = 1;
while (pAequorInstances.length < 30) {
    let instance = pAequorFactory(i, mockUpStrand());
    if (instance.willLikelySurvive()) {
        pAequorInstances.push(instance);
        i++;
    }
}

console.log(pAequorInstances);
