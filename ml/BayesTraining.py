import os, codecs, math

class BayesTraining:
    def __init__(self, trainingdir, stopwordlist):
        self.vocabulary = {}
        self.prob = {}
        self.totals = {}
        self.stopwords = {}
        f = open(stopwordlist)
        for line in f:
            self.stopwords[line.strip()] = 1
        f.close()
        categories = os.listdir(trainingdir)
        # filter out files that are not directories
        self.categories = [filename for filename in categories
                           if os.path.isdir(trainingdir + filename)]

        print("Counting ...")
        for category in self.categories:
            #print('    category: ' + category)
            (self.prob[category],
             self.totals[category]) = self.train(trainingdir, category)
        # I am going to eliminate any word in the vocabulary
        # that doesn't occur at least 3 times
        toDelete = []
        for word in self.vocabulary:
            if self.vocabulary[word] < 3:
                # mark word for deletion
                # can't delete now because you can't delete
                # from a list you are currently iterating over
                toDelete.append(word)
        # now delete
        for word in toDelete:
            del self.vocabulary[word]
        # now compute probabilities
        vocabLength = len(self.vocabulary)
        # print("Computing probabilities:")
        for category in self.categories:
            # print('    ' + category)
            denominator = self.totals[category] + vocabLength
            for word in self.vocabulary:
                if word in self.prob[category]:
                    count = self.prob[category][word]
                else:
                    count = 1
                self.prob[category][word] = (float(count + 1)
                                             / denominator)
                # print ("DONE TRAINING\n\n")

    def train(self, trainingdir, category):
        """counts word occurrences for a particular category"""
        currentdir = trainingdir + category
        files = os.listdir(currentdir)
        counts = {}
        total = 0
        files = os.listdir(trainingdir + category)
        # print("   " + currentBucket)
        for file in files:
            f = codecs.open(currentdir + '//' + file, 'r', 'utf-8')
            for line in f:
                tokens = line.split()
                for token in tokens:
                    # get rid of punctuation and lowercase token
                    token = token.strip('\'".,?:-')
                    for char in token:
                        if char != ' ' and not char in self.stopwords:
                            self.vocabulary.setdefault(char, 0)
                            self.vocabulary[char] += 1
                            counts.setdefault(char, 0)
                            counts[char] += 1
                            total += 1
            f.close()

        return (counts, total)

    def classify(self, content):
        results = {}
        for category in self.categories:
            results[category] = 0

        token = content.strip('\'".,?:-').lower()
        for char in token:
            if char in self.vocabulary:
                for category in self.categories:
                    if self.prob[category][char] == 0:
                        print("%s %s" % (category, char))
                    results[category] += math.log(
                        self.prob[category][char])

        results = list(results.items())
        results.sort(key=lambda tuple: tuple[1], reverse=True)
        # for debugging I can change this to give me the entire list
        return results[0][0]

    def testClassify(self, dir):
        allResult = {}
        for category in self.categories:
            allResult[category] = {"correct": 0, "wrong": 0}
            currentdir = dir + "//" + category
            files = os.listdir(currentdir)
            for file in files:
                filePath = currentdir + '//' + file
                f = codecs.open(filePath, 'r', 'utf-8')
                content = f.readline()
                print(content)
                result = self.classify(content)
                print(category + "/" + file + ": " + result)
                if result == category:
                    allResult[category]["correct"] += 1
                else:
                    allResult[category]["wrong"] += 1

        return allResult


prefixPath = "D://Workspace//pythonWorkspace//python_gentleman_crawler//data//vr//"
theDir = prefixPath + "training//"
stoplistfile = prefixPath + "stopwords.txt"
testDir = prefixPath + "test//"
bt = BayesTraining(theDir, stoplistfile)
#print(bt.vocabulary)
#print(bt.prob)

#print(bt.classify("犯されたアイドル あやみ旬果"))
#print(bt.classify("ボクを好き過ぎるボクだけの従順ペット 2 鈴村あいり"))
print(bt.testClassify(testDir))
